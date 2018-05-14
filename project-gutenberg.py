#!/usr/bin/env python3

import sys
import re
import os
import argparse

from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from gutenberg.query import get_etexts
from gutenberg._domain_model.exceptions import InvalidCacheException

from markdown import markdown
from bs4 import BeautifulSoup

from utils import splitIntoWords, filter_numbers, maybe_normalize, extract_sentences, check_output_dir

def remove_markup(t):
    return ''.join(BeautifulSoup(markdown(t), 'html.parser').findAll(text=True))

def get_books_by_lang():
    try:
        return list(get_etexts('language', 'fr'))
    except InvalidCacheException:
        print("""
    You need to create a Gutenberg cache first:
    Run those in your venv:

python -c 'from gutenberg.acquire import get_metadata_cache; get_metadata_cache().populate();'

    It might take a few hours.
                """)
        return list()

mapping_specific = [
  [ u'N.-N.-E.', u'nord-nord-est'    ],
  [ u'E.-N.-E.', u'est-nord-est'     ],
  [ u'E.-N.-O.', u'est-nord-est'     ],
  [ u'E.-S.-E.', u'est-sud-est'      ],
  [ u'S.-S.-E.', u'sud-sud-est'      ],
  [ u'S.-S.-O.', u'sud-sud-ouest'    ],
  [ u'O.-S.-O.', u'ouest-sud-ouest'  ],
  [ u'O.-N.-O.', u'ouest-nord-ouest' ],
  [ u'N.-N.-O.', u'nord-nord-ouest'  ],
  [ u'N.-E.',    u'nord-est'   ],
  [ u'S.-E.',    u'sud-est'    ],
  [ u'S.-O.',    u'sud-ouest'  ],
  [ u'N.-O.',    u'nord-ouest' ],
  [ u' N.',      u' nord'  ],
  [ u' S.',      u' sud'   ],
  [ u' E.',      u' est'   ],
  [ u' O.',      u' ouest' ],
  [ u'\'N.',     u'\'nord'  ],
  [ u'\'S.',     u'\'sud'   ],
  [ u'\'E.',     u'\'est'   ],
  [ u'\'O.',     u'\'ouest' ],
]

def parse_one_book(bookid):
    this_line = 0
    has_title = False
    mainpage_marker    = '    '
    has_mainpage       = False
    has_start_mainpage = False
    has_end_mainpage   = False
    
    finaltext = []
    for line in remove_markup(strip_headers(load_etext(bookid)).strip()).split('\n'):
        this_line += 1
        
        if len(line) == 0:
            continue
    
        if not has_title:
            if line.startswith(mainpage_marker):
                if line.isupper():
                    has_title = True
                    #print('FOUND TITLE @', this_line, "'{}'".format(line))
            continue
    
        if not has_mainpage:
            if not has_start_mainpage:
                if line.startswith(mainpage_marker):
                    has_start_mainpage = True
                    #print('FOUND MAIN PAGE START @', this_line, "'{}'".format(line))
                continue
            else:
                if not line.startswith(mainpage_marker):
                    has_end_mainpage = True
                    #print('FOUND MAIN PAGE END @', this_line, "'{}'".format(line))
                else:
                    continue
    
            has_mainpage = has_start_mainpage and has_end_mainpage
    
        if line.startswith('  '):
            #print('FOUND SOME EXTRA @', this_line, "'{}'".format(line))
            continue
    
        if line.isupper():
            #print('FOUND ONE CHAPTER @', this_line, "'{}'".format(line))
            continue
    
        line = maybe_normalize(line)
        line = maybe_normalize(line, mapping=mapping_specific)
        line = filter_numbers(line)
    
        finaltext += [ line ]

    return finaltext

parser = argparse.ArgumentParser(description='Project Gutenberg text content extraction for Common Voice')
parser.add_argument('--one', action='store_true', default=False, help='Stop after the first file written.')
parser.add_argument('--dry', action='store_true', default=False, help='Dry run, do not write any data file.')

parser.add_argument('--min-words', type=int, default=2, help='Minimum number of words to accept a sentence')
parser.add_argument('--max-words', type=int, default=45, help='Maximum number of words to accept a sentence')
parser.add_argument('--numbooks', type=int, default=100, help='Number of books to process')

parser.add_argument('output', type=str, help='Output directory')

args = parser.parse_args()
check_output_dir(args.output)

print('Querying index')
for book in get_books_by_lang()[:args.numbooks]:
    print('Treating bookid #{}'.format(book))

    sentences = extract_sentences(parse_one_book(book), args.min_words, args.max_words)

    output_book_name = os.path.join(args.output, "{}.txt".format(book))
    print('output_book_name', output_book_name)
    if not args.dry:
        with open(output_book_name, 'w') as output_book:
            bytes = output_book.write('.\n'.join(sentences))
            if bytes == 0:
                print('Empty content for bookid #{}'.format(book))
    else:
        print('.\n'.join(sentences))

    if args.one:
        break
