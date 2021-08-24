# -*- coding: utf-8 -*-
#
# This script parses the README.md and generates a machine-readable
# data structure from it, for publication as an API.
#
# https://springload.github.io/awesome-wagtail/api/v1/readme.json
#
# It is automatically ran as part of Travis builds, also validating the README
# formatting, and the API endpoint is deployed on successful builds on master.
#
# See also:
# - https://djangopackages.org/api/v3/grids/wagtail-cms/
# - https://github.com/awesomerank/rank

from __future__ import absolute_import, unicode_literals

import json
import codecs
import datetime

API_PATH = '/api/v1/readme.json'


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
        'tools': parse_subsections(cut_section('Tools')),
        'resources': parse_subsections(cut_section('Resources')),
        'sites': parse_section(cut_section('Open-source sites')),
        'metadata': {
            'updated': '%sZ' % datetime.datetime.utcnow().isoformat(),
        },
    }


if __name__ == '__main__':
    readme = open('README.md', 'r').read()

    try:
        parsed_readme = parse_readme(readme)
        json_path = './dist%s' % API_PATH

        with codecs.open(json_path, mode='w+', encoding='utf8') as f:
            readme_payload = json.dumps(parsed_readme, indent=True, ensure_ascii=False)
            print(readme_payload)
            f.write(readme_payload)
    except:
        print('Is the README well formatted?')
        raise
