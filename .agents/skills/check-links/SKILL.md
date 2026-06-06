---
name: check-links
description: Guides the automated archival workflow of awesome links. Fetching links data, moving stale entries.
license: CC0
metadata:
  audience: maintainers
  # Hide the skill from discovery: https://github.com/vercel-labs/skills#optional-fields
  internal: true
  disable-model-invocation: true
---

## Overview

Analyze and maintain links in the README. Fetches metadata for each link, detects stale entries, auto-updates GitHub repo titles and descriptions, and produces a structured report for archival decisions.

## Requirements

- **Python 3.12+** with [`uv`](https://docs.astral.sh/uv/)
- **`gh` CLI** authenticated (`gh auth status`)
- Network access for HTTP requests (httpx)

## Available scripts

- **`scripts/check_links.py`** — Fetches metadata for all links in `README.md` and generates a Markdown report on stdout.

## Workflow

### 1. Run the link checker

```bash
./scripts/check_links.py --dry-run
```

Always run with `--dry-run` first to preview changes without modifying
the README. Re-run without `--dry-run` to auto-update GitHub repo titles
and descriptions when you're ready.

Add `--verbose` to see progress and API call details on stderr.

The database is stored at `.awesome-wagtail.duckdb` by default. Subsequent
runs reuse cached data (24 h for GitHub, 30 d for web pages).

### 2. Read the report

The report printed to stdout is your action plan. It contains these sections:

#### Auto-Archive Candidates (GitHub)

Repos that are **archived on GitHub** or **have not been pushed to in over
24 months**. These should be moved to `docs/archive.md` and removed from
`README.md`.

#### Needs Review — 12–24 months (GitHub)

Repos with no commits in 12–24 months. For each entry, check whether the
repo's GitHub page or its entry in `README.md` mentions "archived",
"deprecated", or "unmaintained". If so, move to archive. If the repo is
still active despite infrequent commits, leave it in place.

#### Updated Link Titles (GitHub)

Repo link titles that differ from the project name found in the repo's
README heading. Review the list — many README headings contain badge
markup or instructions rather than a clean project name. Only update
titles that are clearly better.

#### Updated Link Descriptions (GitHub)

Repo descriptions that differ from GitHub's project description. In most
cases the GitHub description is shorter and more accurate. Apply these
updates to `README.md`.

#### Auto-Archive Candidates (web pages)

Pages that have not been updated in over 5 years (based on HTTP
`Last-Modified` headers, `<meta>` tags, or schema.org data). Move these
to `docs/archive.md`.

#### Title Mismatches (web pages)

Page titles in `README.md` that differ from the actual `<h1>` or
`<title>` of the page. Review and update if the fetched title is a
better description of the link.

### 3. Create or update the archive file

The archive lives at `docs/archive.md`. Mirror the same section structure
as `README.md` (section > subsection). For each archived link:

1. Remove the line from `README.md`
2. Add the line under the matching section in `docs/archive.md`

If the archive file does not exist yet, create it with:

```markdown
# Awesome Wagtail Archive

> Archived projects from the main README that are no longer actively maintained.

## Apps

### Blogging/news

... archived items moved here ...
```

### 4. Commit changes

When finished, review the diff and commit:

```bash
git diff
git add -A
git commit -m "check-links: archive stale entries and update metadata" --trailer "Assisted-by: <Agent harness> (<Model name>)"
```
