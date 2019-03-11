#!/usr/bin/env python3
import sys
import re
import os
import argparse
import requests

from bs4 import BeautifulSoup, Comment
from random import shuffle

from utils import splitIntoWords, filter_numbers, maybe_normalize, extract_sentences, check_output_dir, set_custom_boundaries
import spacy
try:
    import fr_core_news_sm #if it doesn't work, an alternative is: nlp = spacy.load('fr_core_news_sm') https://spacy.io/models/fr. See also line nlp = fr_core_news_sm.load(), at the bottom of the page
    nlp = fr_core_news_sm.load()   #if it doesn't work, try: nlp = spacy.load('fr_core_news_sm'). See  imports, and https://spacy.io/models/fr, https://spacy.io/models/fr, etc.
except ModuleNotFoundError:
    from spacy.cli import download as spacy_model_download
    spacy_model_download('fr_core_news_sm')
    nlp = spacy.load('fr_core_news_sm')

    import nltk
    nltk.download('punkt')

# - prose
# - 19è + 20è siècle
LIBRETHEATRE_URL = 'https://data.libretheatre.fr/ajax?__fromnavigation=1&rql=DISTINCT+Any+X%2CA%2CX%2CG%2CX%2CF%2CM%2CW+ORDERBY+XAT+WHERE+X+genre+G%2C+A+author_of+X%2C+X+preferred_form+XA%2C+X+text_form+F%2C+XA+title+XAT%2C+X+nb_men+M%2C+X+nb_women+W%2C+X+text_form+%22Prose%22%2C+X+timespan+B%2C+B+eid+IN(1742%2C+3181)&__force_display=1&vid=table.work.no-filter&divid=table_work_no_filter_28fab344fb3a4775b10b359c84710a16&fname=view&pageid=1403154733050406ce179a062b74023961c80756d6f8349'
WORK_TEMPLATE = 'https://data.libretheatre.fr/work/%(workid)d'
PD_LICENCE = 'https://data.libretheatre.fr/license/1747'

mapping_specific = [
  [ u'(', u''],
  [ u')', u''],
  [ re.compile('\. $'), u'.' ],
  [ re.compile(' \.'), u'.' ],
  [ u' ,  ', u', ' ],
  [ u' , ', u', ' ],
  [ u'  ', u' ' ],
  [ u'--', u' ' ],
  [ re.compile('\.{2,}'),   u'\u00a0\u2026' ],
  [ re.compile('\s?\n\s?'), u' '],
  [ u'  ', u' ' ],
]

PUNCT_NBSP = re.compile('(\w+)(\?|\!|;|:)')

def parse_result_page(page):
    content = requests.get(page)

    if not content.status_code == 200:
        raise

    html = BeautifulSoup(content.content, 'html.parser')

    listing = html.findAll('table', class_='listing')

    if not listing:
        raise

    entries = listing[0].findAll('tbody')[0].findAll('tr')

    if not entries:
        raise

    all = []
    for e in entries:
        all_a = e.findAll('a')

        work_a = list(filter(lambda x: '/work/' in x.get('href'), all_a))
        assert len(work_a) == 1

        work_id = int(work_a[0].get('href').split('/work/')[1])
        assert work_id > 0

        all.append(work_id)

    return all

def fetch_play_text(url):
    text = []

    if url and len(url) > 0:
        if 'libretheatre.fr' in url:
            text = fetch_play_text_libretheatre(url)
        elif 'wikisource.org' in url:
            text = fetch_play_text_wikisource(url)

    finaltext = []
    for line in text:
        line = maybe_normalize(line)
        line = maybe_normalize(line, mapping=mapping_specific)
        line = filter_numbers(line)
        line = line.strip()

        maybe_matches = re.finditer(PUNCT_NBSP, line)
        for maybe_match in maybe_matches:
            line = line.replace(maybe_match.group(0), "%s\u00a0%s" % (maybe_match.group(1), maybe_match.group(2)))

        finaltext += [ line ]

    return finaltext

def fetch_play_text_libretheatre(url):
    return ''

def fetch_play_text_wikisource(url):
    content = requests.get(url)
    if not content.status_code == 200:
        raise

    html = BeautifulSoup(content.content, 'html.parser')

    for comments in html.findAll(text=lambda text:isinstance(text, Comment)):
        comments.extract()

    content = html.findAll('div', class_='mw-parser-output')
    assert len(content) == 1

    for _class in [ 'mw-headline', 'ws-noexport', 'mw-editsection' ]:
        for e in content[0].findAll(class_=_class):
            e.decompose()

    return list(filter(lambda x: x != '\n', content[0].findAll(text=True)))

def get_one_play(id):
    assert id > 0
    play_url = WORK_TEMPLATE % { 'workid': id }

    content = requests.get(play_url)
    if not content.status_code == 200:
        if content.status_code == 404:
            print('URL returned 404: %s' % play_url)
        else:
            raise Exception('HTTP error code: %d' % content.status_code)

    html = BeautifulSoup(content.content, 'html.parser')

    entry = html.findAll('table', class_='cw-table-primary-entity')
    if not entry:
        raise
    assert len(entry) == 1

    is_public_domain = False

    src = None
    rows = entry[0].findAll('tr')
    for row in rows:
        th = row.findAll('th')[0]
        td = row.findAll('td')[0]

        if th.text == 'licence':
            try:
                if td.findAll('a')[0].get('href') == 'https://data.libretheatre.fr/license/1747':
                    is_public_domain = True
                else:
                    raise ValueError('Non Public-Domain licence: %s' % td.get('href'))
            except IndexError:
                pass

        if th.text == 'domaine public':
            if td.text == 'oui':
                is_public_domain = True

        if th.text == 'texte en ligne':
            try:
                url = td.findAll('a')[0].get('href')
            except IndexError:
                raise ValueError('No valid URL available')

            # Check attachment
            if 'libretheatre.fr' in url:
                attachments = html.findAll('div', class_='rsetbox')
                for attach in attachments:
                    title = attach.findAll('div', class_='panel-heading')
                    if title[0].text != 'pièce jointe':
                        continue

                    attachment = attach.findAll('div', class_='panel-body')
                    assert len(attachment) == 1

                    src = attachment[0].findAll('a')[0].get('href')

                    raise ValueError('LibreTheatre URL: %s' % play_url)

            # Looks like WikiSource
            elif 'wikisource' in url:
                src = url

            else:
                raise ValueError('Unsupported URL:', url)

    if not is_public_domain:
        raise ValueError('Non Public-Domain licence.')

    return fetch_play_text(src)


def dump_one_play(play,nlp=None):
    print('Treating playid #{}'.format(play))
    try:
        sentences = list(extract_sentences(get_one_play(play), args.min_words, args.max_words, nlp=nlp))
        nb_sents = len(sentences)

        if nb_sents < 2:
            print('Too few content: %d. Check %s' % (nb_sents, WORK_TEMPLATE % { 'workid': play }))
            return

        output_play_name = os.path.join(args.output, "{}.txt".format(play))
        print('output_play_name', output_play_name)
        if not args.dry:
            with open(output_play_name, 'wb') as output_play:
                bytes = output_play.write('\n'.join(sentences).encode('utf-8'))
                if bytes == 0:
                    print('Empty content for playid #{}'.format(play))
        else:
            print('\n'.join(sentences))
    except ValueError as e:
        print('Unable to fetch play because of', e)


parser = argparse.ArgumentParser(description='LibreTheatre text content extraction for Common Voice')
parser.add_argument('--one', action='store_true', default=False, help='Stop after the first file written.')
parser.add_argument('--this', type=int, default=-1, help='Fetch this specific ID')
parser.add_argument('--dry', action='store_true', default=False, help='Dry run, do not write any data file.')

parser.add_argument('--min-words', type=int, default=3, help='Minimum number of words to accept a sentence')
parser.add_argument('--max-words', type=int, default=15, help='Maximum number of words to accept a sentence')

parser.add_argument('output', type=str, help='Output directory')

args = parser.parse_args()
check_output_dir(args.output)

if args.this == -1:
    all_ids = parse_result_page(LIBRETHEATRE_URL)
else:
    all_ids = [ args.this ]

if args.one:
    all_ids = [ all_ids[0] ]


nlp.add_pipe(set_custom_boundaries, before='parser') 
for entry in all_ids:
    dump_one_play(entry, nlp)
