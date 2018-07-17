#!/usr/bin/env python3

import re
import os
import argparse
import datetime

from xml.dom.pulldom import START_ELEMENT, CHARACTERS, END_ELEMENT, parse
from xml.dom.minidom import Element, Text

from utils import splitIntoWords, filter_numbers, recursive_text, extract_sentences, check_output_dir

parser = argparse.ArgumentParser(description='SyceronBrut text content extraction for Common Voice')
parser.add_argument('--one', action='store_true', default=False, help='Stop after the first file written.')
parser.add_argument('--dry', action='store_true', default=False, help='Dry run, do not write any data file.')

parser.add_argument('--min-words', type=int, default=3, help='Minimum number of words to accept a sentence')
parser.add_argument('--max-words', type=int, default=15, help='Maximum number of words to accept a sentence')

parser.add_argument('file', type=str, help='Source XML file')
parser.add_argument('output', type=str, help='Output directory')

args = parser.parse_args()
check_output_dir(args.output)

doc = parse(args.file)
indent_level = 0
visited = []

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
      visited.append(node)

      if node.tagName == "DateSeance":
        if seance_context is not None and 'texte' in seance_context:
          output_seance_name = os.path.join(args.output, seance_context['DateSeance'])
          if os.path.isfile(output_seance_name + '.txt'):
            output_seance_name += str(int(datetime.datetime.timestamp(datetime.datetime.utcnow())))

          output_seance_name += '.txt'
          print('output_seance_name', output_seance_name)
          sentences = extract_sentences(seance_context['texte'], args.min_words, args.max_words)
          if not args.dry:
            with open(output_seance_name, 'w') as output_seance:
              output_seance.write('.\n'.join(sentences))
          else:
            print('.\n'.join(sentences))

          if args.one:
            break

        doc.expandNode(node)
        date_seance = node.firstChild.nodeValue

        if len(date_seance) != 17:
            print("Bogus DateSeance?", date_seance)
            continue

        seance_context = { 'DateSeance':  date_seance }

  if event == END_ELEMENT:
    indent_level -= 2
    if type(node) == Element and len(visited) > 0:
      old = visited.pop()
      del old

  if node.nodeName == 'texte' and seance_context is not None and 'DateSeance' in seance_context:
    doc.expandNode(node)

    if visited[-2].attributes and 'code_style' in visited[-2].attributes and visited[-2].attributes['code_style'].value == 'NORMAL':
      fullText = filter_numbers(recursive_text(node))
      fullText = re.compile('\s+').sub(' ', fullText)
      try:
        seance_context[node.nodeName].append(fullText)
      except KeyError:
        seance_context[node.nodeName] = [ fullText ]
