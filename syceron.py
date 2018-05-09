#!/usr/bin/env python3

import sys
import re
import os
import argparse
import networkx as nx
import networkx.drawing.nx_pydot as nx_pydot
import datetime
from num2words import num2words

from xml.dom.pulldom import START_ELEMENT, CHARACTERS, END_ELEMENT, parse
from xml.dom.minidom import Element, Text

parser = argparse.ArgumentParser(description='SyceronBrut text content extraction for Common Voice')
parser.add_argument('--one', action='store_true', default=False, help='Stop after the first file written.')

parser.add_argument('--print-tree', action='store_true', help='Only print XML tree structure')
parser.add_argument('--tree-output', type=argparse.FileType('w'), help='Where to store XML tree structure. Use \'-\' for stdout.')

parser.add_argument('--dry', action='store_true', default=False, help='Dry run, do not write any data file.')

parser.add_argument('--min-words', type=int, default=2, help='Minimum number of words to accept a sentence')
parser.add_argument('--max-words', type=int, default=45, help='Maximum number of words to accept a sentence')

parser.add_argument('file', type=str, help='Source XML file')
parser.add_argument('output', type=str, help='Output directory')

args = parser.parse_args()

doc = parse(args.file)
indent_level = 0
visited = []

structure = nx.DiGraph()

is_syceron = False

accepted_seance_context = [
  re.compile("CompteRendu@Metadonnees@DateSeance"),
  re.compile("CompteRendu@Metadonnees@Sommaire@Sommaire1@TitreStruct@Intitule"),
  re.compile("CompteRendu@Contenu@Quantiemes@Journee"),
  #re.compile("CompteRendu@Contenu@ouverture_seance@paragraphe@ORATEURS@ORATEUR@NOM"),
  re.compile(".*@paragraphe@texte$"),
]
seance_context = None

accepted_code_style = [
  'NORMAL'
]

mapping_normalization = [
  [ u'\xa0 ', u' ' ],
  [ u'«\xa0', u'«' ],
  [ u'\xa0»', u'»' ],
  [ u'\xa0' , u' ' ],
  [ u'M. '  , u'Monsieur ' ],
  [ u'Mme ' , u'Madame ' ],
  [ u'Mlle ' , u'Mademoiselle ' ],
  [ u'Mlles ', u'Mademoiselles ' ],
  [ u'%', u'pourcent' ],
]

superscript_chars_mapping = {
  '0': u'\u2070',
  '1': u'\u00b9',
  '2': u'\u00b2',
  '3': u'\u00b3',
  '4': u'\u2074',
  '5': u'\u2075',
  '6': u'\u2076',
  '7': u'\u2077',
  '8': u'\u2078',
  '9': u'\u2079',

  '0 ': u'\u2070 ',
  '1 ': u'\u00b9 ',
  '2 ': u'\u00b2 ',
  '3 ': u'\u00b3 ',
  '4 ': u'\u2074 ',
  '5 ': u'\u2075 ',
  '6 ': u'\u2076 ',
  '7 ': u'\u2077 ',
  '8 ': u'\u2078 ',
  '9 ': u'\u2079 ',

  'o': 'uméro',
  'os': 'uméros',

  'o ': 'uméro ',
  'os ': 'uméros ',
  's ': 's ',
  ' ': '',
  'ter': 'ter',

  # Those should be in sync with ORDINAL_REGEX
  'e': 'ieme',
  'è': 'ieme ',
  'èm': 'ieme ',
  'e ': 'ieme ',
  'e –': 'ieme –',
  'er': 'ier',
  'er ': 'ier ',
  'er.': 'ier.',
  'er,': 'ier,',
  'ER': 'ier',
  'Er': 'ier',
  'er –': 'ier –',
  're': 'iere',
  'ère': 'iere',
  'ère': 'iere',
  'ème': 'ieme',
  'éme': 'ieme',
  'ème ': 'ieme',
  'eme': 'ieme',
}

ORDINAL_REGEX = re.compile("(\d+)([ieme|ier|iere]+)")

subscript_chars_mapping = {
  '0': u'\u2080',
  '1': u'\u2081',
  '2': u'\u2082',
  '3': u'\u2083',
  '4': u'\u2084',
  '5': u'\u2085',
  '6': u'\u2086',
  '7': u'\u2087',
  '8': u'\u2088',
  '9': u'\u2089',

  '0 ': u'\u2080 ',
  '1 ': u'\u2081 ',
  '2 ': u'\u2082 ',
  '3 ': u'\u2083 ',
  '4 ': u'\u2084 ',
  '5 ': u'\u2085 ',
  '6 ': u'\u2086 ',
  '7 ': u'\u2087 ',
  '8 ': u'\u2088 ',
  '9 ': u'\u2089 ',

  'e': u'\u2091',
  ' ': '',
}

WORD_REGEX = re.compile("[^\w\d\'\-]+")
def splitIntoWords(text):
    return WORD_REGEX.split(text)

NUMS_REGEX = re.compile("(\d+,?\u00A0?\d+)|(\d+\w+)|(\d)*")
def getNumbers(text):
    return NUMS_REGEX.split(text)

if not os.path.isdir(args.output):
  print('Directory does not exists', args.output, file=sys.stderr)
  sys.exit(1)

for event, node in doc:
  if not is_syceron:
    if event == START_ELEMENT:
      is_syceron = node.tagName == "syceronBrut"
    continue

  if event == CHARACTERS:
    if type(node) == Text:
      if not node.nodeValue.isprintable():
        continue

  if event == START_ELEMENT:
    indent_level += 2
    if type(node) == Element:
      if args.print_tree and len(visited) > 0:
        structure.add_edge(visited[-1].tagName, node.tagName)

      visited.append(node)

      if node.tagName == "DateSeance":
        if seance_context is not None and 'texte' in seance_context:
          output_seance_name = os.path.join(args.output, seance_context['DateSeance'])
          if os.path.isfile(output_seance_name + '.txt'):
            output_seance_name += str(int(datetime.datetime.timestamp(datetime.datetime.utcnow())))

          output_seance_name += '.txt'
          print('output_seance_name', output_seance_name)
          raw_sentences = (' '.join(seance_context['texte'])).split('. ')
          sentences = filter(lambda x: len(splitIntoWords(x)) >= args.min_words and len(splitIntoWords(x)) <= args.max_words, raw_sentences)
          if not args.dry:
            with open(output_seance_name, 'w') as output_seance:
              output_seance.write('.\n'.join(sentences))
          else:
            print('.\n'.join(sentences))

          if args.one:
            break

        doc.expandNode(node)
        seance_context = { 'DateSeance':  node.firstChild.nodeValue }

  if event == END_ELEMENT:
    indent_level -= 2
    if type(node) == Element and len(visited) > 0:
      old = visited.pop()
      del old

  if node.nodeName == 'texte':
    doc.expandNode(node)

    def filter_numbers(inp):
      finalinp = ''

      for e in getNumbers(inp):
        if not e:
          continue

        newinp = e
        #print('filter_numbers', 'e=', e)

        try:
          ee = ''.join(e.split())
          if int(e) > 0:
            #print('filter_numbers', 'INT:BEFORE', 'ee=', ee, 'newinp=', newinp)
            newinp = num2words(int(ee), lang='fr')
            #print('filter_numbers', 'INT:AFTER', 'ee=', ee, 'newinp=', newinp)
        except ValueError:
          try:
            ee = ''.join(e.replace(',', '.').split())
            if float(ee):
              #print('filter_numbers', 'FLOAT:BEFORE', 'ee=', ee, 'newinp=', newinp)
              newinp = num2words(float(ee), lang='fr')
              #print('filter_numbers', 'FLOAT:AFTER', 'ee=', ee, 'newinp=', newinp)
          except ValueError:
            matches = ORDINAL_REGEX.match(e)
            if matches:
              newinp = num2words(int(matches.group(1)), ordinal=True, lang='fr')

        finalinp += newinp

        #print('filter_numbers', 'e=', e, 'newinp=', newinp, 'finalinp=', finalinp)

      return finalinp

    def maybe_normalize(value):
      for norm in mapping_normalization:
        value = value.replace(norm[0], norm[1])
      return filter_numbers(value)

    def maybe_translate(element, mapping):
      value = maybe_normalize(element.nodeValue)

      if value in mapping:
        return mapping[value]

      print("NOT TRANSLATED: '{}' => '{}'".format(element.nodeValue, value))
      for c in value:
        print("value: '{}' == {}".format(c, ord(c)))
      return value

    def recursive_text(root, finaltext=""):
      if root.nodeName == 'br':
        return ' '
      else:
        for c in root.childNodes:
          if c.nodeType == c.TEXT_NODE:
            if root.nodeName == 'exposant':
              finaltext += maybe_translate(c, superscript_chars_mapping)
            elif root.nodeName == 'indice':
              finaltext += maybe_translate(c, subscript_chars_mapping)
            else:
              finaltext += maybe_normalize(c.nodeValue)
          if c.nodeType == c.ELEMENT_NODE:
            finaltext += recursive_text(c)
      return finaltext

    if visited[-2].attributes and 'code_style' in visited[-2].attributes and visited[-2].attributes['code_style'].value == 'NORMAL':
      fullText = recursive_text(node)
      try:
        seance_context[node.nodeName].append(fullText)
      except KeyError:
        seance_context[node.nodeName] = [ fullText ]

if args.tree_output:
  print(nx_pydot.to_pydot(structure), file=sys.stdout if args.tree_output == '-' else args.tree_output)
