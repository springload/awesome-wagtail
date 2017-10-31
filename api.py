# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import json


def parse_line(line, category):
    name = line.split('](')[0][3:]
    url = line.split('](')[1].split(')')[0]
    description = '' if line[-1] == ')' else line.split(') ')[1][2:]

    return {
        'name': name,
        'description': description,
        'url': url,
        'category': category,
    }


def parse_section(section, category=''):
    return [parse_line(l, category) for l in section.split('\n')]


def parse_subsections(section):
    subsections = section.split('### ')[1:]

    items = []

    for subsection in subsections:
        split_section = subsection.split('\n\n')
        section_title = split_section[0]

        items += parse_section(split_section[1], section_title)

    return items


def cut_section(start):
    return readme.split('## %s\n\n' % start)[1].split('\n\n## ')[0]


def parse_readme(readme):
    return {
        'apps': parse_subsections(cut_section('Apps')),
        'tools': parse_section(cut_section('Tools')),
        'resources': parse_subsections(cut_section('Resources')),
        'sites': parse_section(cut_section('Open-source sites')),
    }


if __name__ == '__main__':
    readme = open('README.md', 'r').read()
    readme_payload = parse_readme(readme)

    with open('./dist/api/v1/readme.json', mode='w+', encoding='utf-8') as f:
        f.write(json.dumps(readme_payload, indent=True))
