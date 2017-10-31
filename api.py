# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import json


def parse_line(line, category):
    name = line.split('](')[0][3:]
    description = line.split(') ')[1][2:]
    url = line.split('](')[1].split(') ')[0]

    return {
        'name': name,
        'description': description,
        'url': url,
        'category': category,
    }

def parse_apps(readme):
    app_section = readme.split('## Apps')[1].split('## Tools')[0]
    app_sections = app_section.split('### ')[1:]

    apps = []

    for section in app_sections:
        split_section = section.split('\n\n')
        section_title = split_section[0]

        for line in split_section[1].split('\n'):
            app = parse_line(line, section_title)
            apps.append(app)

    return apps


def parse_readme(readme):
    return {
        'apps': parse_apps(readme),
    }


if __name__ == '__main__':
    readme = open('README.md', 'r').read()
    readme_payload = parse_readme(readme)

    with open('./dist/api/v1/readme.json', mode='w+', encoding='utf-8') as f:
        f.write(json.dumps(readme_payload, indent=True))
