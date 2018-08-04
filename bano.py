import argparse
import csv
import glob
import os
import random
import re
import subprocess
from _sha1 import sha1

from utils import check_output_dir, mapping_normalization, maybe_normalize, filter_numbers, splitIntoWords

TEMPLATES = [
    '{number} {street_lower}, {zipcode} {city}',
    '{number} {street_lower}, {zipcode_alt}, {city}',
    '{number} {street_lower}, {zipcode_alt} à {city}',
    '{street}, {zipcode} {city}',
    '{street}, {zipcode_alt} {city}',
    '{street}, {city}',
    '{street} à {city}',
    '{number} {street_lower}',
    '{street} au numéro {number}',
]


normalizers = [
    # convert "001" -> "0 0 1"
    # NB: do it 3 times since we may have we may have multiple successive zeros
    (re.compile(r'(\s|^)0(\d+)(\s|$|,)', flags=re.IGNORECASE), r'\g<1>0 \g<2>\g<3>'),
    (re.compile(r'(\s|^)0(\d+)(\s|$|,)', flags=re.IGNORECASE), r'\g<1>0 \g<2>\g<3>'),
    (re.compile(r'(\s|^)0(\d+)(\s|$|,)', flags=re.IGNORECASE), r'\g<1>0 \g<2>\g<3>'),
    # convert "23C" -> "23 C"
    (re.compile(r'(\s|^)(\d+)([a-z]+)(\s|$|,)', flags=re.IGNORECASE), r'\g<1>\g<2> \g<3>\g<4>'),
] + mapping_normalization + [
    # "à Le Havre" => "au Havre"
    (re.compile(r'\sà le\s', flags=re.IGNORECASE), ' au '),
    (re.compile(r'\sà les\s', flags=re.IGNORECASE), ' aux '),
    # NB: replace remaining "0"s that are ignored by num2words
    (re.compile(r'(\s|^)0(\s|$|,)'), r'\g<1>zéro\g<2>'),
    (re.compile(r'(\s|^)0(\s|$|,)'), r'\g<1>zéro\g<2>'),
]


def format_address(address, template):
    # NB: zipcode is sometime pronounced in 3 parts
    # ex: 75001 => soixante quinze zero zero un
    # and sometime pronounced in 2 parts
    # ex: 01090 => zero un quatre vingt dix
    # see unit tests for more info

    zipcode = address['zipcode']

    zipcode_alt = '{}{}, {}{}{}'.format(*zipcode)
    address.update(
        zipcode=zipcode_alt if zipcode.startswith('0') else zipcode,
        zipcode_alt=zipcode_alt,
    )

    str = template.format(
        street_lower='{}{}'.format(address['street'][0].lower(), address['street'][1:]),
        **address
    )

    str = maybe_normalize(str, mapping=normalizers)
    str = filter_numbers(str)
    return str.strip()


if __name__ == "__main__":
    # execute only if run as a script
    parser = argparse.ArgumentParser(description='French addresses extraction for Common Voice')
    # parser.add_argument('--one', action='store_true', default=False, help='Stop after the first file written.')
    # parser.add_argument('--this', type=int, default=-1, help='Fetch this specific ID')
    parser.add_argument('--dry', action='store_true', default=False, help='Dry run, do not write any data file.')

    parser.add_argument('--min-words', type=int, default=3, help='Minimum number of words to accept a sentence')
    parser.add_argument('--max-words', type=int, default=15, help='Maximum number of words to accept a sentence')
    parser.add_argument('--max-lines', type=int, default=5000, help='Maximum number of addresses per file')

    parser.add_argument('output', type=str, help='Output directory')
    parser.add_argument('--tmp-dir', type=str, help='Location directory', default='/tmp/bano')

    args = parser.parse_args()
    check_output_dir(args.output)

    if not os.path.isdir(args.tmp_dir):
        os.mkdir(args.tmp_dir)
    # download BANO if not done yet
    if not os.path.isfile(os.path.join(args.tmp_dir, 'LICENCE.txt')):
        print('Start downloading BANO from http://bano.openstreetmap.fr/data/. May take a while')
        subprocess.run(
            'wget -r --no-parent http://bano.openstreetmap.fr/data/ -l1 -A.txt,.csv -nd --no-verbose -P'.split(' ') + [args.tmp_dir]
        )

    csv_headers = ['id', 'number', 'street', 'zipcode', 'city']

    found_streets = set()  # avoid streets with same name
    filenames = [
        f for f in sorted(glob.glob(os.path.join(args.tmp_dir, '*.csv')))
        if os.path.basename(f) != 'code_cadastre.csv'
    ]

    for filename in filenames:
        output_file_name = os.path.basename(filename).replace('bano', 'addresses')
        output_path = os.path.join(args.output, output_file_name)
        count = 0
        addresses_str = []
        with open(filename) as csvfile:
            print('Start reading {}'.format(filename))
            reader = csv.DictReader(csvfile, delimiter=',', fieldnames=csv_headers)
            addresses = list(reader)
        random.Random(1234).shuffle(addresses)
        for address in addresses:
            street_hash = sha1(address['street'].encode()).hexdigest()
            if not address['street'] or not address['zipcode'] or not address['number'] or street_hash in found_streets:
                continue

            template_index = count % len(TEMPLATES)

            clean_sentence = format_address(address, TEMPLATES[template_index])
            n_tokens = len(splitIntoWords(clean_sentence))
            if n_tokens < args.min_words or n_tokens > args.max_words:
                continue
            if args.dry:
                print(clean_sentence)
            else:
                addresses_str.append(clean_sentence)

            count += 1
            found_streets.add(street_hash)
            if args.max_lines and count > args.max_lines:
                break
        if not args.dry:
            with open(output_path, 'w') as outfile:
                outfile.write('\n'.join(addresses_str))


