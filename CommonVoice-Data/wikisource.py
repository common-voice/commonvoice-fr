#coding: utf-8

import os
import re
import argparse
import unicodedata
import subprocess

import ebooklib
from ebooklib import epub

import nltk
from nltk import word_tokenize,sent_tokenize

from bs4 import BeautifulSoup
import spacy
from lxml import etree

from collections import Counter
from utils import splitIntoWords, filter_numbers, maybe_normalize, extract_sentences, check_output_dir, set_custom_boundaries

# URL file EPUB
EPUB_LINK = 'https://tools.wmflabs.org/wsexport/tool/book.php?lang=fr&format=epub&page=Les_Forceurs_de_blocus'

#filename temporary
FILENAME_TMP = 'temp.epub'

# list of XHTML files not to be taken into account
EXCLUDE_FILE = [
    'about.xhtml',
    'cover.xhtml',
    'nav.xhtml',
    'title.xhtml',
]

# mapping for abbr tags
ABBRS_MAPPING = {
    'ADN': 'acide désoxyribonucléique',
    'BD': 'bande dessinée',
    'CD': 'compact disc',
    'CRS': 'compagnies républicaines de sécurité',
    'C.V.': 'curriculum vitæ',
    'DTC': 'dans ton cul',
    'DRM': 'gestion des droits numériques',
    'EDF': 'Électricité de France',
    'FAI': 'fournisseur d\'accès internet',
    'FMI': 'Fonds Monétaire International',
    'HD': 'haute définition',
    'HLM': 'habitation à loyer modéré',
    'IRL': 'In Real Life',
    'IVG': 'interruption volontaire de grossesse',
    'GIGN': 'groupe d\'intervention de la Gendarmerie nationale',
    'LGBT': 'lesbiennes, gays, bisexuels et transgenres',
    'ONG': 'organisation non gouvernementale',
    'ORTF': 'office de radiodiffusion-télévision française',
    'QG': 'quartier général',
    'PIB': 'produit intérieur brut',
    'PMU': 'pari mutuel urbain',
    'PS': 'parti Socialiste',
    'PQ': 'papier toilette',
    'RER': 'réseau express régional',
    'THC': 'tétrahydrocannabinol',
    'SAV': 'service après-vente',
    'SDF': 'sans domicile fixe',
    'SNCF': 'société nationale des chemins de fer français',
    'USA': 'États-Unis d\'Amérique',
    'TER': 'train express régionale',
    'TGV': 'train grande vitesse',
    'VF': 'version française',
    'VMC': 'ventilation mécanique contrôlée',
    'V.O.I.P.': 'voix sur IP',
    'WC': 'toilettes',
}

# mapping in all the text
MAPPING_WORDS = {
    '#': '', # remove hashtags from Pouhiou's novels
    'NdP': '', # remove "note de pouhiou"
    '()': '',
    '. .': '.', # rest from hashtags deletion
    'NdT': 'Note du traducteur',
    'NDT': 'Note du traducteur',
    '°': ' degré',
}

# remove tags with class="hashtag" for the following epub titles
TITLES_REMOVE_HASHTAGS = [
    '#Smartarded',
    '#MonOrchide. Le Cycle des NoéNautes, II',
    # Apolog ok
]

# the characters to be deleted before saving the file
REMOVE_CHARACTERS = [
    'TABLE DES MATIÈRES.',
    '^',
    ' 1.',' 2.',' 3.',' 4.',' 5.',' 6.',' 7.',' 8.',' 9.',' 10.',
    ' 11.',' 12.',' 13.',' 14.',' 15.',' 16.',' 17.',' 18.',' 19.',' 20.',
    ' 21.',' 22.',' 23.',' 24.',' 25.',' 26.',' 27.',' 28.',' 29.',' 30.',
]


def remove_subtree(selector):
    """
    Remove subtrees from a BeautifulSoup selector
    """
    if selector:
        [x.extract() for x in selector]

def clean_html(soup, remove_hashtags = False):
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
    # remove bibliography
    remove_subtree(soup.find_all(attrs={"epub:type": "biblioentry"}))
    for item in soup.find_all('li'): # empty list items
        if re.match(r'^[ \;\-\.]+$', item.get_text()):
            item.extract()
    # remove special formating from Pouhiou's novels
    remove_subtree(soup.find_all('code'))
    if remove_hashtags:
        remove_subtree(soup.find_all(attrs={"class": "hashtag"}))
    # replace abbreviations
    for k,v in ABBRS_MAPPING.items():
        abbrs_items = soup.find_all('abbr', string=k)
        for item in abbrs_items:
            item.string = v
    return soup

def clean_epub_item(item, abbr: bool, code: bool, remove_hashtags:bool = False):
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
    soup_cleaned = clean_html(soup, remove_hashtags)
    # remove_markup
    plaintext = ''.join(soup_cleaned.find_all(text=True))
    # mapping words
    for k,v in MAPPING_WORDS.items():
        plaintext = plaintext.replace(k, v)
    return plaintext, abbrs

def parse_epub(filename: str, abbr: bool, code: bool):
    """
    Parse an epub file
    """

    book = epub.read_epub(filename)
    title = book.get_metadata('DC', 'title')[0][0]
    remove_hashtags = title in TITLES_REMOVE_HASHTAGS # indicate to remove hashtags
    print('\nParsing book "{0}"'.format(title))
    list_plaintexts = []
    counter_abbrs = Counter()
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        name = item.get_name()
        if name in EXCLUDE_FILE:
            print('...Ignoring {0}'.format(name))
            continue
        print('...Parsing {0}'.format(name))
        # parse and clean chapter
        plaintext, abbrs = clean_epub_item(item, abbr, code, remove_hashtags)
        list_plaintexts.append(plaintext)
        counter_abbrs += Counter(abbrs)

    book_plaintext = '\n\n\n'.join(list_plaintexts)
    # replace numbers
    book_plaintext = filter_numbers(book_plaintext)
    # normalize
    book_plaintext = maybe_normalize(book_plaintext)
    if abbr:
        print('Abbreviation counts:\n{0}'.format(counter_abbrs.items()))

    return book_plaintext

def clean_sentence(string: str):
    """
    Clean one sentence
    """
    # normalize
    string = unicodedata.normalize("NFKD", string)
    string = string.lstrip(' -—»|') # didascalies and others
    string = string.replace('\n', ' ')
    return string

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
    # Remove characters useless
    for tag in REMOVE_CHARACTERS:
        string = string.replace(tag,'')

    if inputdir == '-1':
        # contruction filename export
        a,b = EPUB_LINK.split('page=',1)
        new_name = filename.replace(filename, outputdir + '/' + b.replace ('+','-') + '.txt')
        os.remove(filename)
        filename = new_name
    else:
        # construction file and save
        filename = filename.replace(inputdir, outputdir)
        filename = filename.replace('.epub', '.txt')

    with open(filename, 'w') as f:
        f.write(string)


def main(
        inputdir: str,
        outputdir: str,
        minwords: int = 3,
        maxwords: int = 14,
        one: bool = False,
        dry: bool = False,
        abbr: bool = False,
        code: bool = False,
        plaintext: bool = False):
    try:
        nlp = spacy.load('fr_core_news_sm')
        # add max length for the sentence
        nlp.max_length = 5000000
        nlp.add_pipe(set_custom_boundaries, before='parser')
    except OSError:
        raise OSError('French model not installed. Please run:\n'\
                      'python -m spacy download fr_core_news_sm')

    if inputdir == '-1':
        # download file
        subprocess.call(['wget', '-O', FILENAME_TMP, EPUB_LINK,'--no-check-certificate'])
        filenames = [FILENAME_TMP]
    else:
        # list file directory
        filenames = list_files(inputdir)

    for filename in filenames:
        text = parse_epub(filename, abbr, code)
        if plaintext:
            string_final = text
        else:
            # extract sentences using utils module
            sentences = extract_sentences([text],
                min_words=minwords, max_words=maxwords, nlp=nlp)
            # clean and filter sentences
            sentences = [clean_sentence(x) for x in sentences]
            string_final = '\n'.join(list(sentences))
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

    parser.add_argument('--plaintext', action='store_true', default=False, help='Extract plain text. If False, write extracted sentences.')

    parser.add_argument('inputdir', type=str, help='Input directory OR -1 for URL file')
    parser.add_argument('outputdir', type=str, help='Output directory')

    args = parser.parse_args()

    # if it is different from -1 then the EPUB file is in the DATA folder
    # if it is -1 we will call the url of the variable EPUB_LINK
    if args.inputdir != '-1':
        check_output_dir(args.inputdir)

    check_output_dir(args.outputdir)

    return vars(args)

if __name__ == '__main__':
    args = parse_arguments()
    main(**args)
