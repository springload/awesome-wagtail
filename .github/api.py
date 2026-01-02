"""
This script parses the README.md and generates a machine-readable
data structure from it, for publication as an API.

https://springload.github.io/awesome-wagtail/api/v1/readme.json

It is automatically ran as part of Travis builds, also validating the README
formatting, and the API endpoint is deployed on successful builds on master.

See also:
- https://djangopackages.org/api/v3/grids/wagtail-cms/
- https://github.com/awesomerank/rank
"""

import json
from datetime import datetime, timezone
from pathlib import Path

API_PATH = '/api/v1/readme.json'


def parse_line(line: str, category: str) -> dict[str, str]:
    """Parse a single line from the README into a structured dictionary."""
    print(line)
    name = line.split('](')[0][3:]
    url = line.split('](')[1].split(')')[0]
    description = '' if line[-1] == ')' else line.split(') ')[1][2:]

    return {
        'name': name,
        'description': description,
        'url': url,
        'category': category,
    }


def parse_section(section: str, category: str = '') -> list[dict[str, str]]:
    """Parse a section of lines into a list of structured items."""
    return [parse_line(line, category) for line in section.split('\n')]


def parse_subsections(section: str) -> list[dict[str, str]]:
    """Parse a section containing multiple subsections."""
    subsections = section.split('### ')[1:]

    items = []

    for subsection in subsections:
        split_section = subsection.split('\n\n')
        section_title = split_section[0]

        items += parse_section(split_section[1], section_title)

    return items


def cut_section(readme: str, start: str) -> str:
    """Extract a specific section from the README."""
    return readme.split(f'## {start}\n\n')[1].split('\n\n## ')[0]


def parse_readme(readme: str) -> dict:
    """Parse the entire README into a structured dictionary."""
    return {
        'apps': parse_subsections(cut_section(readme, 'Apps')),
        'tools': parse_subsections(cut_section(readme, 'Tools')),
        'resources': parse_subsections(cut_section(readme, 'Resources')),
        'sites': parse_section(cut_section(readme, 'Open-source sites')),
        'metadata': {
            'updated': datetime.now(timezone.utc).isoformat(),
        },
    }


if __name__ == '__main__':
    readme_path = Path('README.md')

    try:
        readme = readme_path.read_text(encoding='utf-8')
        parsed_readme = parse_readme(readme)

        json_path = Path(f'./dist{API_PATH}')
        json_path.parent.mkdir(parents=True, exist_ok=True)

        readme_payload = json.dumps(parsed_readme, indent=2, ensure_ascii=False)
        print(readme_payload)

        json_path.write_text(readme_payload, encoding='utf-8')

    except FileNotFoundError as e:
        print(f'Error: Could not find file - {e}')
        raise
    except (KeyError, IndexError) as e:
        print(f'Error: README formatting issue - {e}')
        print('Is the README well formatted?')
        raise
    except Exception as e:
        print(f'Unexpected error: {e}')
        raise
