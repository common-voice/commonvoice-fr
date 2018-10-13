import argparse
import csv
import re
import string
from collections import defaultdict
from pathlib import Path
from marshmallow import Schema, fields, validate

import utils

ARCHIVE_PREFIX = 'cv_'
FIRSTNAMES_ARCHIVE_NAME = 'nat2017'
FIRSTNAMES_ARCHIVE_DIR_NAME = ARCHIVE_PREFIX + FIRSTNAMES_ARCHIVE_NAME
FIRSTNAMES_ARCHIVE_URL = 'https://www.insee.fr/fr/statistiques/fichier/2540004/nat2017_txt.zip'

LASTNAME_ARCHIVE_NAME = 'noms2008nat_txt'
LASTNAME_ARCHIVE_DIR_NAME = ARCHIVE_PREFIX + LASTNAME_ARCHIVE_NAME
LASTNAME_ARCHIVE_URL = 'https://www.insee.fr/fr/statistiques/fichier/3536630/noms2008nat_txt.zip'

TEMPLATES = [
    "{firstname:capitalize_name} {lastname:capitalize_name}",
    "{gender:capitalize} {firstname:capitalize_name} {lastname:capitalize_name}",
    "{gender:capitalize} {lastname:capitalize_name}, {firstname:capitalize_name} {lastname:capitalize_name}",
    "{firstname:capitalize_name} {firstname:spell_name}",
    "{lastname:capitalize_name} {lastname:spell_name}",
    "{firstname:capitalize_name} {lastname:capitalize_name} {lastname:spell_name}",
    "mon nom c'est {firstname:capitalize_name} {lastname:capitalize_name} {lastname:spell_name}",
    "{lastname:capitalize_name}, ça s'épelle {lastname:spell_name}",
    "{lastname:capitalize_name}, ça s'écrit {lastname:spell_name}",
    "nom {lastname:capitalize_name}, prénom {firstname:capitalize_name}",
]
NAME_SEP_REGEX = re.compile(r'(.+)([-\s])(.+)')
REPEATED_CHAR_REGEX = re.compile(r'(\s.*?)\1+')


def capitalize_name(name: str):
    if not NAME_SEP_REGEX.match(name):
        return name.capitalize()

    def _capitalize(match):
        return f'{capitalize_name(match.group(1))}{match.group(2)}{capitalize_name(match.group(3))}'
    return NAME_SEP_REGEX.sub(_capitalize, name)


def spell_name(name: str):
    def replace_duplicates(match):
        return ' deux' + match.group(1)
    name = ' '.join('plus loin' if char in {' ', '-'} else char.upper() for char in name)
    return REPEATED_CHAR_REGEX.sub(replace_duplicates, name)


class FirstnameSchema(Schema):
    year = fields.Integer(required=True, load_from='annais')
    gender = fields.Integer(required=True, load_from='sexe')  # 1=Male, 2=Female
    count = fields.Integer(required=True, load_from='nombre')
    firstname = fields.String(required=True, load_from='preusuel', validate=validate.Length(min=2))


class LastnameSchema(Schema):
    lastname = fields.String(required=True, load_from='NOM', validate=validate.Length(min=2))
    _1891_1900 = fields.Integer(required=True)
    _1901_1910 = fields.Integer(required=True)
    _1911_1920 = fields.Integer(required=True)
    _1921_1930 = fields.Integer(required=True)
    _1931_1940 = fields.Integer(required=True)
    _1941_1950 = fields.Integer(required=True)
    _1951_1960 = fields.Integer(required=True)
    _1961_1970 = fields.Integer(required=True)
    _1971_1980 = fields.Integer(required=True)
    _1981_1990 = fields.Integer(required=True)
    _1991_2000 = fields.Integer(required=True)


def get_most_common_lastnames(file_: Path, count=5000):
    lastnames = defaultdict(int)
    with file_.open(encoding='utf-8-sig') as f:
        csv_reader = csv.DictReader(f, delimiter='\t')
        items, errors = LastnameSchema().load(list(csv_reader), many=True)

    for i, item in enumerate(items):
        if i in errors or item['lastname'] == 'AUTRES NOMS':
            continue
        lastnames[item['lastname'].lower()] += (
            item['_1891_1900'] +
            item['_1901_1910'] +
            item['_1911_1920'] +
            item['_1921_1930'] +
            item['_1931_1940'] +
            item['_1941_1950'] +
            item['_1951_1960'] +
            item['_1961_1970'] +
            item['_1971_1980'] +
            item['_1981_1990'] +
            item['_1991_2000']
        )
    return [
        name
        for name, count in sorted(lastnames.items(), key=lambda x: -x[1])
    ][:count]


def get_most_common_firstnames(file_: Path, count=5000):
    firstnames = defaultdict(lambda: dict(c=0, gm=0, gf=0))
    with file_.open(encoding='utf-8-sig') as f:
        csv_reader = csv.DictReader(f, delimiter='\t')
        items, errors = FirstnameSchema().load(list(csv_reader), many=True)
    for i, item in enumerate(items):
        if i in errors:
            continue
        firstname = item['firstname'].lower()
        if firstname == '_prenoms_rares':
            continue
        current = firstnames[firstname]
        current['c'] += item['count']
        if item['gender'] == 1:
            current['gm'] += item['count']
        elif item['gender'] == 2:
            current['gf'] += item['count']
        else:
            raise NotImplementedError
    # compute gender
    for firstname, data in firstnames.items():
        is_male_prob = data['gm'] / float(data['gf'] + data['gm'])
        if is_male_prob > 0.98:
            data.update(gender='monsieur')
        elif is_male_prob < 0.02:
            data.update(gender='madame')

    return [
        (name, data['gender'])
        for name, data in sorted(firstnames.items(), key=lambda x: -x[1]['c'])
        if data.get('gender')
    ][:count]


class CustomFormatter(string.Formatter):
    def format_field(self, value, format_spec):
        format_fn = {
            'capitalize': lambda x: x.capitalize(),
            'capitalize_name': capitalize_name,
            'spell_name': spell_name,
        }.get(format_spec)
        if format_fn:
            return format_fn(value)
        return super().format_field(value, format_spec)


if __name__ == "__main__":
    # execute only if run as a script
    parser = argparse.ArgumentParser(description='French names extraction for Common Voice')
    parser.add_argument('--dry', action='store_true', default=False, help='Dry run, do not write any data file.')
    parser.add_argument('--max-lines', type=int, default=5000, help='Maximum number of lines')

    parser.add_argument('output', type=str, help='Output file')
    parser.add_argument('--tmp-dir', type=str, help='Location directory', default='/tmp/')

    args = parser.parse_args()

    # download data
    output_file = Path(args.output)
    target_dir = Path(args.tmp_dir)

    firstnames_archive_path = utils.maybe_download(ARCHIVE_PREFIX + FIRSTNAMES_ARCHIVE_NAME + '.zip', target_dir, FIRSTNAMES_ARCHIVE_URL)
    utils.maybe_extract(firstnames_archive_path, target_dir / FIRSTNAMES_ARCHIVE_DIR_NAME)
    extracted_firstnames_file = target_dir / f'{ARCHIVE_PREFIX}{FIRSTNAMES_ARCHIVE_NAME}/{FIRSTNAMES_ARCHIVE_NAME}.txt'

    lastnames_archive_path = utils.maybe_download(ARCHIVE_PREFIX + LASTNAME_ARCHIVE_NAME + '.zip', target_dir, LASTNAME_ARCHIVE_URL)
    utils.maybe_extract(lastnames_archive_path, target_dir / LASTNAME_ARCHIVE_DIR_NAME)
    extracted_lastnames_file = target_dir / f'{ARCHIVE_PREFIX}{LASTNAME_ARCHIVE_NAME}/{LASTNAME_ARCHIVE_NAME}.txt'

    # read files
    print('extract lastnames')
    lastnames = get_most_common_lastnames(extracted_lastnames_file, count=args.max_lines)
    print('extract firstnames')
    firstnames = get_most_common_firstnames(extracted_firstnames_file, count=args.max_lines)
    print('generate sentences')
    formatter = CustomFormatter()
    sentences = [
        formatter.format(TEMPLATES[i % len(TEMPLATES)], lastname=lastname, firstname=firstname, gender=gender)
        for i, ((firstname, gender), lastname) in enumerate(zip(firstnames, lastnames))
    ]
    if args.dry:
        print(sentences)
    else:
        with output_file.open('w') as f:
            f.writelines('\n'.join(sentences))
