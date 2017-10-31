# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import json


def parse_line(line, category):
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


def parse_apps(readme):
    section = readme.split('## Apps\n\n')[1].split('\n\n## Tools')[0]
    subsections = section.split('### ')[1:]

    apps = []

    for subsection in subsections:
        split_section = subsection.split('\n\n')
        section_title = split_section[0]

        for line in split_section[1].split('\n'):
            app = parse_line(line, section_title)
            apps.append(app)

    return apps


def parse_tools(readme):
    section = readme.split('## Tools\n\n')[1].split('\n\n## Resources')[0]

    tools = []

    for line in section.split('\n'):
        tool = parse_line(line, '')
        tools.append(tool)

    return tools


def parse_resources(readme):
    section = readme.split('## Resources\n\n')[1].split('\n\n## Community')[0]
    subsections = section.split('### ')[1:]

    resources = []

    for subsection in subsections:
        split_section = subsection.split('\n\n')
        section_title = split_section[0]

        for line in split_section[1].split('\n'):
            resource = parse_line(line, section_title)
            resources.append(resource)

    return resources


def parse_sites(readme):
    section = readme.split('## Open-source sites\n\n')[1].split('\n\n## Contribute')[0]

    sites = []

    for line in section.split('\n'):
        site = parse_line(line, '')
        sites.append(site)

    return sites


def parse_readme(readme):
    return {
        'apps': parse_apps(readme),
        'tools': parse_tools(readme),
        'resources': parse_resources(readme),
        'sites': parse_sites(readme),
    }


if __name__ == '__main__':
    readme = open('README.md', 'r').read()
    readme_payload = parse_readme(readme)

    with open('./dist/api/v1/readme.json', mode='w+', encoding='utf-8') as f:
        f.write(json.dumps(readme_payload, indent=True))
