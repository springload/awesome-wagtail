#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "httpx>=0.27",
#   "beautifulsoup4>=4.12",
#   "duckdb>=1.0",
#   "lxml",
# ]
# ///

"""
Check links in README.md — fetch metadata, detect stale entries, and auto-update
GitHub repo titles and descriptions.

Usage:
  .agents/skills/check-links/scripts/check_links.py [OPTIONS]

Options:
  --readme PATH       Path to README.md (default: README.md)
  --db PATH           DuckDB database path (default: .awesome-wagtail.duckdb)
  --dry-run           Don't modify files, only report
  --verbose           Print progress to stderr
  --help              Show this message
"""

import argparse
import base64
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import duckdb
import httpx
from bs4 import BeautifulSoup

REPO_CACHE_MAX_AGE = timedelta(hours=24)
PAGE_CACHE_MAX_AGE = timedelta(days=30)

STALE_12_MONTHS = timedelta(days=365)
STALE_24_MONTHS = timedelta(days=730)
STALE_5_YEARS = timedelta(days=1825)

SKIP_SECTIONS = {"Contents", "Contribute", "License"}


def parse_date_utc(date_str: str | None) -> datetime | None:
    if not date_str:
        return None
    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc)
        return dt
    except (ValueError, TypeError):
        try:
            dt = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z")
            return dt.replace(tzinfo=timezone.utc)
        except (ValueError, TypeError):
            return None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check links in README.md and fetch metadata."
    )
    parser.add_argument(
        "--readme",
        default="README.md",
        help="Path to README.md (default: README.md)",
    )
    parser.add_argument(
        "--db",
        default=".awesome-wagtail.duckdb",
        help="DuckDB database path (default: .awesome-wagtail.duckdb)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Don't modify files, only report",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print progress to stderr",
    )
    return parser.parse_args()


def log(msg: str, verbose: bool = False) -> None:
    if verbose:
        print(msg, file=sys.stderr)


# ── README Parsing (adapted from .github/api.py) ──────────────────────


def parse_line(
    line: str, section: str, subsection: str | None
) -> dict[str, str] | None:
    line = line.strip()
    if not line.startswith("- [") and not line.startswith("– ["):
        return None
    match = re.match(r"^[-–] \[([^\]]+)\]\(([^\)]+)\)(?:\s*[-–]\s*(.*))?$", line)
    if not match:
        return None
    name = match.group(1)
    url = match.group(2)
    description = (match.group(3) or "").strip()
    category = f"{section} > {subsection}" if subsection else section
    return {
        "name": name,
        "url": url,
        "description": description,
        "section": section,
        "subsection": subsection,
        "category": category,
    }


def parse_readme_links(readme: str) -> list[dict[str, str]]:
    lines = readme.split("\n")
    links: list[dict[str, str]] = []
    current_section: str | None = None
    current_subsection: str | None = None

    for line in lines:
        if line.startswith("## ") and not line.startswith("### "):
            heading = line[2:].strip()
            if heading in SKIP_SECTIONS:
                current_section = None
                current_subsection = None
            else:
                current_section = heading
                current_subsection = None
        elif line.startswith("### ") and current_section:
            current_subsection = line[4:].strip()
        elif line.startswith("- [") or line.startswith("– ["):
            if current_section:
                link = parse_line(line, current_section, current_subsection)
                if link:
                    links.append(link)
    return links


# ── URL Classification ──────────────────────────────────────────────


def is_youtube_url(url: str) -> bool:
    return bool(re.search(r"(youtube\.com|youtu\.be)", url))


def is_github_url(url: str) -> bool:
    return bool(re.match(r"https?://github\.com/", url))


def extract_github_repo(url: str) -> tuple[str, str] | None:
    match = re.match(r"https?://github\.com/([^/]+)/([^/#\?]+)", url)
    if match:
        owner = match.group(1)
        repo = match.group(2).replace(".git", "")
        return owner, repo
    return None


# ── DuckDB Cache ──────────────────────────────────────────────────


def init_db(db_path: str) -> duckdb.DuckDBPyConnection:
    con = duckdb.connect(db_path)
    con.execute("""
        CREATE TABLE IF NOT EXISTS link_metadata (
            url VARCHAR PRIMARY KEY,
            link_type VARCHAR,
            category VARCHAR,
            fetched_at TIMESTAMP,
            repo_full_name VARCHAR,
            repo_description VARCHAR,
            star_count INTEGER,
            pushed_at VARCHAR,
            is_archived BOOLEAN,
            readme_content VARCHAR,
            project_name VARCHAR,
            topics VARCHAR,
            page_title VARCHAR,
            h1_title VARCHAR,
            meta_description VARCHAR,
            author VARCHAR,
            page_last_updated VARCHAR
        )
    """)
    # Migrate old schema: rename tags -> topics if needed
    try:
        con.execute("ALTER TABLE link_metadata DROP COLUMN tags")
    except Exception:
        pass
    try:
        con.execute("ALTER TABLE link_metadata ADD COLUMN topics VARCHAR")
    except Exception:
        pass
    return con


def get_cached(
    con: duckdb.DuckDBPyConnection, url: str, max_age: timedelta
) -> dict[str, Any] | None:
    row = con.execute(
        "SELECT * FROM link_metadata WHERE url = ? AND fetched_at > ?",
        [url, datetime.now(timezone.utc) - max_age],
    ).fetchone()
    if row is None:
        return None
    columns = [desc[0] for desc in con.description]
    return dict(zip(columns, row))


def set_cached(con: duckdb.DuckDBPyConnection, url: str, data: dict[str, Any]) -> None:
    columns = list(data.keys())
    placeholders = ", ".join(["?" for _ in columns])
    col_names = ", ".join(columns)
    values = [data.get(col) for col in columns]
    con.execute(
        f"INSERT OR REPLACE INTO link_metadata ({col_names}) VALUES ({placeholders})",
        values,
    )


# ── GitHub Metadata Fetching ─────────────────────────────────────


def run_gh(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["gh"] + args,
        capture_output=True,
        text=True,
        check=False,
    )


def fetch_github_batch(repos: list[tuple[str, str, str]]) -> dict[str, dict[str, Any]]:
    """Fetch metadata for a batch of GitHub repos via GraphQL.

    Args:
        repos: list of (url, owner, repo) tuples
    Returns:
        dict of url -> metadata dict
    """
    if not repos:
        return {}

    query_parts = []
    alias_map: dict[str, str] = {}

    for i, (url, owner, repo) in enumerate(repos):
        alias = f"r{i}"
        alias_map[alias] = url
        query_parts.append(
            f'  {alias}: repository(owner: "{owner}", name: "{repo}") {{\n'
            f"    name\n"
            f"    description\n"
            f"    stargazerCount\n"
            f"    pushedAt\n"
            f"    isArchived\n"
            f"    url\n"
            f"    repositoryTopics(first: 10) {{\n"
            f"      nodes {{\n"
            f"        topic {{\n"
            f"          name\n"
            f"        }}\n"
            f"      }}\n"
            f"    }}\n"
            f"  }}"
        )

    query = "{\n" + "\n".join(query_parts) + "\n}"
    result = run_gh(["api", "graphql", "-f", f"query={query}"])

    if result.returncode != 0:
        log(f"  GraphQL error: {result.stderr[:300]}", verbose=True)
        return {}

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        log(f"  JSON parse error in GraphQL response", verbose=True)
        return {}

    url_to_repo = {url: (owner, repo) for url, owner, repo in repos}

    results: dict[str, dict[str, Any]] = {}
    errors = data.get("errors", [])
    if errors:
        for err in errors:
            log(f"  GraphQL error: {err.get('message', '')}", verbose=True)

    for alias, url in alias_map.items():
        repo_data = data.get("data", {}).get(alias)
        if repo_data is None:
            results[url] = {"error": "Repository not found"}
        else:
            owner, repo_name = url_to_repo.get(url, ("", ""))
            topic_nodes = (repo_data.get("repositoryTopics") or {}).get("nodes") or []
            topics = [
                n["topic"]["name"]
                for n in topic_nodes
                if n and n.get("topic") and n["topic"].get("name")
            ]
            results[url] = {
                "repo_full_name": f"{owner}/{repo_name}"
                if owner and repo_name
                else None,
                "repo_name": repo_data.get("name"),
                "repo_description": repo_data.get("description"),
                "star_count": repo_data.get("stargazerCount"),
                "pushed_at": repo_data.get("pushedAt"),
                "is_archived": repo_data.get("isArchived"),
                "repo_url": repo_data.get("url"),
                "topics": json.dumps(topics) if topics else None,
            }

    return results


def fetch_github_readme(owner: str, repo: str) -> str | None:
    result = run_gh(["api", f"repos/{owner}/{repo}/readme"])
    if result.returncode != 0:
        return None
    try:
        data = json.loads(result.stdout)
        content = data.get("content", "")
        return base64.b64decode(content).decode("utf-8")
    except (json.JSONDecodeError, Exception):
        return None





def extract_project_name(readme_content: str | None) -> str | None:
    if not readme_content:
        return None
    match = re.search(r"^#\s+(.+)$", readme_content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


# ── Web Page Metadata Fetching ───────────────────────────────────


def fetch_page_metadata(url: str) -> dict[str, Any]:
    metadata: dict[str, Any] = {
        "page_title": None,
        "h1_title": None,
        "meta_description": None,
        "author": None,
        "page_last_updated": None,
    }

    try:
        with httpx.Client(follow_redirects=True, timeout=15.0) as client:
            response = client.get(
                url, headers={"User-Agent": "awesome-wagtail-link-checker/1.0"}
            )
        response.raise_for_status()
    except httpx.HTTPError as e:
        metadata["error"] = str(e)
        return metadata

    soup = BeautifulSoup(response.text, "lxml")

    title_tag = soup.find("title")
    metadata["page_title"] = title_tag.get_text(strip=True) if title_tag else None

    h1 = soup.find("h1")
    metadata["h1_title"] = h1.get_text(strip=True) if h1 else None

    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc and meta_desc.get("content"):
        metadata["meta_description"] = meta_desc["content"].strip()
    else:
        meta_og_desc = soup.find("meta", attrs={"property": "og:description"})
        if meta_og_desc and meta_og_desc.get("content"):
            metadata["meta_description"] = meta_og_desc["content"].strip()

    metadata["author"] = find_author(soup)

    metadata["page_last_updated"] = find_last_updated(soup, response)

    return metadata


def find_author(soup: BeautifulSoup) -> str | None:
    meta_author = soup.find("meta", attrs={"name": "author"})
    if meta_author and meta_author.get("content"):
        return meta_author["content"].strip()

    twitter_creator = soup.find("meta", attrs={"name": "twitter:creator"})
    if twitter_creator and twitter_creator.get("content"):
        return twitter_creator["content"].strip()

    article_author = soup.find("meta", attrs={"property": "article:author"})
    if article_author and article_author.get("content"):
        return article_author["content"].strip()

    rel_author = soup.find("link", attrs={"rel": "author"})
    if rel_author and rel_author.get("href"):
        return rel_author["href"].strip()

    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string)
            if isinstance(data, dict):
                author = data.get("author", {})
                if isinstance(author, dict):
                    return author.get("name")
                elif isinstance(author, str):
                    return author
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        author = item.get("author", {})
                        if isinstance(author, dict):
                            return author.get("name")
        except (json.JSONDecodeError, AttributeError):
            pass

    return None


def find_last_updated(soup: BeautifulSoup, response: httpx.Response) -> str | None:
    for meta_name in ("date", "revised", "dcterms.modified"):
        meta = soup.find("meta", attrs={"name": meta_name})
        if meta and meta.get("content"):
            return meta["content"].strip()

    for meta_prop in ("article:modified_time", "article:published_time"):
        meta = soup.find("meta", attrs={"property": meta_prop})
        if meta and meta.get("content"):
            return meta["content"].strip()

    time_tag = soup.find("time", attrs={"datetime": True})
    if time_tag and time_tag.get("datetime"):
        return time_tag["datetime"].strip()

    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string)
            if isinstance(data, dict):
                modified = data.get("dateModified") or data.get("datePublished")
                if modified:
                    return modified
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        modified = item.get("dateModified") or item.get("datePublished")
                        if modified:
                            return modified
        except (json.JSONDecodeError, AttributeError):
            pass

    if "last-modified" in response.headers:
        return response.headers["last-modified"]

    return None


# ── README Auto-Update for GitHub Repos ──────────────────────────


def auto_update_readme_lines(
    lines: list[str],
    updates: list[dict[str, str]],
) -> list[str]:
    updated = list(lines)
    for upd in updates:
        old_url = upd["url"]
        new_title = upd.get("new_title")
        new_desc = upd.get("new_description")
        for i, line in enumerate(updated):
            if old_url in line:
                link_match = re.match(
                    r"^(\s*[-–]\s*)\[([^\]]+)\]\(([^\)]+)\)(\s*[-–]\s*(.*))?$",
                    line.strip(),
                )
                if link_match:
                    prefix = link_match.group(1)
                    old_desc = (link_match.group(5) or "").strip()
                    if new_title:
                        if new_desc and new_desc != old_desc:
                            updated[i] = (
                                f"{prefix}[{new_title}]({old_url}) - {new_desc}\n"
                            )
                        else:
                            updated[i] = (
                                f"{prefix}[{new_title}]({old_url}) - {old_desc}\n"
                                if old_desc
                                else f"{prefix}[{new_title}]({old_url})\n"
                            )
    return updated


# ── Report Generation ─────────────────────────────────────────────


def generate_report(
    all_links: list[dict[str, Any]],
    today: datetime,
) -> str:
    lines: list[str] = []
    lines.append("# Link Check Report\n")
    lines.append(f"Generated: {today.isoformat()}\n")

    gh_repos = [l for l in all_links if l.get("link_type") == "github"]
    web_links = [l for l in all_links if l.get("link_type") == "web"]
    youtube_links = [l for l in all_links if l.get("link_type") == "youtube"]
    errors = [l for l in all_links if l.get("error")]

    lines.append("## Summary\n")
    lines.append(f"| Metric | Count |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total links | {len(all_links)} |")
    lines.append(f"| GitHub repos | {len(gh_repos)} |")
    lines.append(f"| Web pages | {len(web_links)} |")
    lines.append(f"| YouTube (skipped) | {len(youtube_links)} |")
    lines.append(f"| Errors | {len(errors)} |\n")

    if gh_repos:
        lines.append("## GitHub Repos\n")

        auto_archive = []
        needs_review = []
        active = []
        title_updates = []

        for link in gh_repos:
            pushed_at = link.get("pushed_at")
            is_archived = link.get("is_archived", False)
            stale_date = None
            pushed_date = parse_date_utc(pushed_at)
            if pushed_date:
                stale_date = today - pushed_date

            if link.get("new_title") and link["new_title"] != link.get("name"):
                title_updates.append(link)

            if is_archived:
                auto_archive.append(link)
            elif stale_date and stale_date > STALE_24_MONTHS:
                auto_archive.append(link)
            elif stale_date and stale_date > STALE_12_MONTHS:
                needs_review.append(link)
            else:
                active.append(link)

        if auto_archive:
            lines.append(f"### Auto-Archive Candidates ({len(auto_archive)})\n")
            lines.append(
                "These repos are archived or have not been updated in over 24 months.\n"
            )
            lines.append("| # | Link | Stars | Last Commit | Archived | Category |")
            lines.append("|---|------|-------|-------------|----------|----------|")
            for i, link in enumerate(auto_archive, 1):
                stars = link.get("star_count") or "?"
                pushed = (link.get("pushed_at") or "?")[:10]
                arch = "Yes" if link.get("is_archived") else "No"
                url = link["url"]
                title = link.get("name", "")
                desc = link.get("description", "")
                link_text = f"[{title}]({url})" + (f" - {desc}" if desc else "")
                lines.append(
                    f"| {i} | {link_text} | {stars} | {pushed} | {arch} | {link.get('category', '')} |"
                )
            lines.append("")

        if needs_review:
            lines.append(f"### Needs Review — 12–24 months ({len(needs_review)})\n")
            lines.append(
                "These repos have not been updated in 12–24 months. Check if they mention 'archived' or 'deprecated'.\n"
            )
            lines.append("| # | Link | Stars | Last Commit | Category |")
            lines.append("|---|------|-------|-------------|----------|")
            for i, link in enumerate(needs_review, 1):
                stars = link.get("star_count") or "?"
                pushed = (link.get("pushed_at") or "?")[:10]
                url = link["url"]
                title = link.get("name", "")
                desc = link.get("description", "")
                link_text = f"[{title}]({url})" + (f" - {desc}" if desc else "")
                lines.append(
                    f"| {i} | {link_text} | {stars} | {pushed} | {link.get('category', '')} |"
                )
            lines.append("")

        if active:
            lines.append(f"### Active Repos ({len(active)})\n")
            lines.append("| # | Link | Stars | Last Commit | Archived | Category |")
            lines.append("|---|------|-------|-------------|----------|----------|")
            for i, link in enumerate(active, 1):
                stars = link.get("star_count") or "?"
                pushed = (link.get("pushed_at") or "?")[:10]
                arch = "Yes" if link.get("is_archived") else "No"
                url = link["url"]
                title = link.get("name", "")
                desc = link.get("description", "")
                link_text = f"[{title}]({url})" + (f" - {desc}" if desc else "")
                lines.append(
                    f"| {i} | {link_text} | {stars} | {pushed} | {arch} | {link.get('category', '')} |"
                )
            lines.append("")

        if title_updates:
            lines.append(f"### Updated Link Titles ({len(title_updates)})\n")
            lines.append(
                "The following GitHub repo links had titles auto-updated to match their README project name.\n"
            )
            lines.append("| URL | Old Title | New Title |")
            lines.append("|-----|-----------|-----------|")
            for link in title_updates:
                lines.append(
                    f"| {link['url']} | {link.get('name', '')} | {link.get('new_title', '')} |"
                )
            lines.append("")

        if title_updates:
            lines.append(f"### Updated Link Descriptions ({len(title_updates)})\n")
            lines.append(
                "The following GitHub repo links had descriptions auto-updated to match the GitHub project description.\n"
            )
            lines.append("| URL | Old Description | New Description |")
            lines.append("|-----|-----------------|-----------------|")
            for link in title_updates:
                old_desc = link.get("description", "")
                new_desc = link.get("repo_description", "") or "(none)"
                if old_desc != new_desc:
                    lines.append(f"| {link['url']} | {old_desc} | {new_desc} |")
            lines.append("")

    if web_links:
        lines.append("## Other Links\n")

        auto_archive_web = []
        title_mismatches = []

        for link in web_links:
            last_updated = link.get("page_last_updated")
            updated_date = parse_date_utc(last_updated)
            if updated_date and today - updated_date > STALE_5_YEARS:
                auto_archive_web.append(link)

            page_title = link.get("h1_title") or link.get("page_title")
            old_title = link.get("name", "")
            if (
                page_title
                and old_title
                and old_title not in page_title
                and page_title not in old_title
            ):
                title_mismatches.append(link)

        if auto_archive_web:
            lines.append(
                f"### Auto-Archive Candidates — 5+ years ({len(auto_archive_web)})\n"
            )
            lines.append("These pages have not been updated in over 5 years.\n")
            lines.append("| # | URL | Title | Last Updated | Category |")
            lines.append("|---|-----|-------|-------------|----------|")
            for i, link in enumerate(auto_archive_web, 1):
                title = (
                    link.get("h1_title")
                    or link.get("page_title")
                    or link.get("name", "")
                )
                updated = (link.get("page_last_updated") or "?")[:10]
                url = link["url"]
                lines.append(
                    f"| {i} | [{title}]({url}) | {title} | {updated} | {link.get('category', '')} |"
                )
            lines.append("")

        if title_mismatches:
            lines.append(f"### Title Mismatches ({len(title_mismatches)})\n")
            lines.append("The README link title differs from the page title.\n")
            lines.append("| # | URL | README Title | Page Title |")
            lines.append("|---|-----|-------------|------------|")
            for i, link in enumerate(title_mismatches, 1):
                page_title = link.get("h1_title") or link.get("page_title") or ""
                lines.append(
                    f"| {i} | {link['url']} | {link.get('name', '')} | {page_title} |"
                )
            lines.append("")

    if errors:
        lines.append("## Errors\n")
        lines.append("| URL | Error |")
        lines.append("|-----|-------|")
        for link in errors:
            lines.append(f"| {link['url']} | {link.get('error', 'Unknown')} |")
        lines.append("")

    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────


def main() -> None:
    args = parse_args()
    verbose = args.verbose
    dry_run = args.dry_run

    readme_path = Path(args.readme)
    if not readme_path.exists():
        print(f"Error: README not found at {readme_path}", file=sys.stderr)
        sys.exit(1)

    log(f"Reading {readme_path}...", verbose)
    readme = readme_path.read_text(encoding="utf-8")

    log("Parsing links...", verbose)
    links = parse_readme_links(readme)
    log(f"  Found {len(links)} links", verbose)

    log("Initializing DuckDB cache...", verbose)
    con = init_db(args.db)

    today = datetime.now(timezone.utc)

    classified_links: list[dict[str, Any]] = []

    for link in links:
        url = link["url"]
        if is_youtube_url(url):
            link["link_type"] = "youtube"
            classified_links.append(link)
            continue

        if is_github_url(url):
            link["link_type"] = "github"
        else:
            link["link_type"] = "web"
        classified_links.append(link)

    # ── Fetch GitHub metadata ──────────────────────────────

    gh_links = [l for l in classified_links if l["link_type"] == "github"]
    non_cached_gh: list[dict[str, Any]] = []

    for link in gh_links:
        cached = get_cached(con, link["url"], REPO_CACHE_MAX_AGE)
        if cached:
            link.update(cached)
            link["from_cache"] = True
            log(f"  [cache] {link['url']}", verbose)
        else:
            link["from_cache"] = False
            non_cached_gh.append(link)

    if non_cached_gh:
        log(f"Fetching metadata for {len(non_cached_gh)} GitHub repos...", verbose)
        repo_batches: list[tuple[str, str, str]] = []
        for link in non_cached_gh:
            repo = extract_github_repo(link["url"])
            if repo:
                repo_batches.append((link["url"], repo[0], repo[1]))

        BATCH_SIZE = 50
        for i in range(0, len(repo_batches), BATCH_SIZE):
            batch = repo_batches[i : i + BATCH_SIZE]
            log(
                f"  Batch {i // BATCH_SIZE + 1}/{(len(repo_batches) + BATCH_SIZE - 1) // BATCH_SIZE}",
                verbose,
            )
            batch_results = fetch_github_batch(batch)

            for link in non_cached_gh:
                if link["url"] in batch_results:
                    result = batch_results[link["url"]]
                    if "error" in result:
                        link["error"] = result["error"]
                    else:
                        link.update(result)

            for url, owner, repo in batch:
                result = batch_results.get(url, {})
                if "error" in result:
                    continue

                log(f"  Fetching README for {owner}/{repo}...", verbose)
                readme_content = fetch_github_readme(owner, repo)
                if readme_content:
                    link = next((l for l in non_cached_gh if l["url"] == url), None)
                    if link:
                        link["readme_content"] = readme_content
                        link["project_name"] = extract_project_name(readme_content)

                time.sleep(0.1)

        for link in non_cached_gh:
            cache_data = {
                "url": link["url"],
                "link_type": "github",
                "category": link.get("category", ""),
                "fetched_at": datetime.now(timezone.utc),
                "repo_full_name": link.get("repo_full_name"),
                "repo_description": link.get("repo_description"),
                "star_count": link.get("star_count"),
                "pushed_at": link.get("pushed_at"),
                "is_archived": link.get("is_archived"),
                "readme_content": link.get("readme_content"),
                "project_name": link.get("project_name"),
                "topics": link.get("topics"),
            }
            set_cached(con, link["url"], cache_data)

    # ── Fetch web page metadata ────────────────────────────

    web_links = [l for l in classified_links if l["link_type"] == "web"]
    non_cached_web: list[dict[str, Any]] = []

    for link in web_links:
        cached = get_cached(con, link["url"], PAGE_CACHE_MAX_AGE)
        if cached:
            link.update(cached)
            link["from_cache"] = True
            log(f"  [cache] {link['url']}", verbose)
        else:
            link["from_cache"] = False
            non_cached_web.append(link)

    if non_cached_web:
        log(f"Fetching metadata for {len(non_cached_web)} web pages...", verbose)
        for link in non_cached_web:
            log(f"  Fetching {link['url']}...", verbose)
            page_data = fetch_page_metadata(link["url"])
            link.update(page_data)
            if "error" in page_data:
                log(f"    Error: {page_data['error']}", verbose)

            cache_data = {
                "url": link["url"],
                "link_type": "web",
                "category": link.get("category", ""),
                "fetched_at": datetime.now(timezone.utc),
                "page_title": page_data.get("page_title"),
                "h1_title": page_data.get("h1_title"),
                "meta_description": page_data.get("meta_description"),
                "author": page_data.get("author"),
                "page_last_updated": page_data.get("page_last_updated"),
            }
            set_cached(con, link["url"], cache_data)

            time.sleep(0.2)

    # ── Determine updates for GitHub repos ─────────────────

    desc_updates: list[dict[str, str]] = []
    for link in gh_links:
        new_title = link.get("project_name") or link.get("repo_name")
        new_desc = link.get("repo_description")
        if new_title and new_title != link.get("name"):
            link["new_title"] = new_title
        if new_desc and new_desc != link.get("description"):
            link["new_description"] = new_desc
            desc_updates.append(
                {
                    "url": link["url"],
                    "new_description": new_desc,
                }
            )

    # ── Auto-update README (descriptions only, titles are LLM-reviewable) ──

    if desc_updates and not dry_run:
        log(
            f"Updating {len(desc_updates)} GitHub link descriptions in README...",
            verbose,
        )
        readme_lines = readme.split("\n")
        updated_lines = auto_update_readme_lines(readme_lines, desc_updates)
        readme_path.write_text("\n".join(updated_lines), encoding="utf-8")
        log("  README descriptions updated.", verbose)

    # ── Generate report ─────────────────────────────────────

    report = generate_report(classified_links, today)
    print(report)

    # ── Print cache stats ───────────────────────────────────

    gh_cached = con.execute(
        "SELECT COUNT(*) FROM link_metadata WHERE link_type = 'github'"
    ).fetchone()[0]
    web_cached = con.execute(
        "SELECT COUNT(*) FROM link_metadata WHERE link_type = 'web'"
    ).fetchone()[0]
    log(
        f"\nCache stats: {gh_cached} GitHub repos, {web_cached} web pages stored in {args.db}",
        verbose,
    )

    con.close()


if __name__ == "__main__":
    main()
