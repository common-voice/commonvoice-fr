import os
import re
import argparse

import ebooklib
from ebooklib import epub

from bs4 import BeautifulSoup
from random import shuffle

from collections import Counter
from utils import splitIntoWords, filter_numbers, maybe_normalize, extract_sentences, check_output_dir


# keep only some epub items whose names match the regex
REGEX_CHAPITRE = r'.*ch(apitre)?\-?[0-9]+\.xhtml$'

ABBRS_MAPPING = {
    'DTC': 'Dans Ton Cul',
    'IRL': 'In Real Life',
    'NdP': 'Note de Pouhiou',
    # TODO
}


def remove_subtree(selector):
    """
    Remove subtrees from a BeautifulSoup selector
    """
    if selector:
        [x.extract() for x in selector]

def clean_html(soup):
    """
    Clean an HTML BeautifulSoup tree
    """
    # only keep the body
    soup = soup.find('body')
    # remove titles
    for tag in ['h1','h2','h3','h4','h5']:
        remove_subtree(soup.find_all(tag))
    remove_subtree(soup.find_all(attrs={"epub:type": "bodymatter chapter"}))
    remove_subtree(soup.find_all(attrs={"epub:type": "bodymatter subchapter"}))
    remove_subtree(soup.find_all(attrs={"epub:type": "bodymatter subsubchapter"}))
    # remove table of content
    remove_subtree(soup.find_all(attrs={"epub:type": "bodymatter toc"}))
    remove_subtree(soup.find_all(attrs={"id": "TOC"}))
    # remove footnotes
    remove_subtree(soup.find_all(attrs={"epub:type": "footnote"}))
    remove_subtree(soup.find_all(attrs={"epub:type": "noteref"}))
    # remove special formating from Pouhiou's novels
    remove_subtree(soup.find_all('code'))
    return soup

def clean_epub_item(item, abbr: bool, code: bool):
    """
    Parse and clean an epub item
    """
    content = item.get_content()
    soup = BeautifulSoup(content, 'html.parser')
    # abbr
    abbrs = [x.text for x in soup.find_all('abbr')]
    # print text from code tags
    if code:
        for item in soup.find_all('code'):
            print('<code>: {0}'.format(item.text))
    # clean html
    soup_cleaned = clean_html(soup)
    # remove_markup
    plaintext = ''.join(soup_cleaned.find_all(text=True))
    return plaintext, abbrs

def parse_epub(filename: str, abbr: bool, code: bool):
    """
    Parse an epub file
    """
    book = epub.read_epub(filename)
    title = book.get_metadata('DC', 'title')[0][0]
    print('\nParsing book "{0}"'.format(title))
    list_plaintexts = []
    counter_abbrs = Counter()
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        name = item.get_name()
        if not re.match(REGEX_CHAPITRE, name):
            print('...Ignoring {0}'.format(name))
            continue
        print('...Parsing {0}'.format(name))
        plaintext, abbrs = clean_epub_item(item, abbr, code)
        list_plaintexts.append(plaintext)
        counter_abbrs += Counter(abbrs)
    book_plaintext = '\n\n\n'.join(list_plaintexts)
    if abbr:
        print('Abbreviation counts:\n{0}'.format(counter_abbrs.items()))
    return book_plaintext

def list_files(inputdir: str):
    """
    List epub files from inputdir
    """
    filenames = os.listdir(inputdir)
    filenames = [os.path.join(inputdir, f) for f in filenames if f.endswith(".epub")]
    return filenames

def save_text(string: str, filename: str, inputdir: str, outputdir: str):
    """
    Save string as a txt file
    """
    filename = filename.replace(inputdir, outputdir)
    filename = filename.replace('.epub', '.txt')
    with open(filename, 'w') as f:
        f.write(string)

def main(
        inputdir: str,
        outputdir: str,
        minwords: int = 3,
        maxwords: int = 15,
        one: bool = False,
        dry: bool = False,
        abbr: bool = False,
        code: bool = False,
        sentences: bool = True):
    filenames = list_files(inputdir)
    if one:
        filenames = filenames[0:1]
    for filename in filenames:
        plaintext = parse_epub(filename, abbr, code)
        if sentences:
            # extract sentences using utils module
            sentences = extract_sentences([plaintext],
                min_words=minwords, max_words=maxwords, nlp=None)
            string_final = '\n'.join(list(sentences))
        else:
            string_final = plaintext
        if not dry:
            save_text(string_final, filename, inputdir, outputdir)

def parse_arguments():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Framabook text content extraction for Common Voice')

    parser.add_argument('--minwords', type=int, default=3, help='Minimum number of words to accept a sentence')
    parser.add_argument('--maxwords', type=int, default=15, help='Maximum number of words to accept a sentence')

    parser.add_argument('--one', action='store_true', default=False, help='Stop after the first file written.')
    parser.add_argument('--dry', action='store_true', default=False, help='Dry run, do not write any data file.')
    parser.add_argument('--abbr', action='store_true', default=False, help='Print abbreviations extracted from abbr tags.')
    parser.add_argument('--code', action='store_true', default=False, help='Print deleted text from code tags.')

    parser.add_argument('--sentences', action='store_true', default=True, help='Extract sentences. If False, write plain text.')

    parser.add_argument('inputdir', type=str, help='Input directory')
    parser.add_argument('outputdir', type=str, help='Output directory')

    args = parser.parse_args()
    check_output_dir(args.inputdir)
    check_output_dir(args.outputdir)
    return vars(args)

if __name__ == '__main__':
    args = parse_arguments()
    main(**args)
