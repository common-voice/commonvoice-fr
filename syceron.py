#!/usr/bin/env python3

import sys
import re
import os
import argparse
import networkx as nx
import networkx.drawing.nx_pydot as nx_pydot
import json

from xml.dom.pulldom import START_ELEMENT, CHARACTERS, END_ELEMENT, parse
from xml.dom.minidom import Element, Text

parser = argparse.ArgumentParser(description='SyceronBrut text content extraction for Common Voice')
parser.add_argument('--debug', action='store_true', help='Some debug')
parser.add_argument('--debug-more', action='store_true', help='Some more debug')

parser.add_argument('--print-tree', action='store_true', help='Only print XML tree structure')
parser.add_argument('--tree-output', type=argparse.FileType('w'), help='Where to store XML tree structure. Use \'-\' for stdout.')

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

chars_mapping = {
  'o': 'uméro',
  'o ': 'uméro',
  'os ': 'uméros',
}

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
        structure.add_edge(visited[-1], node.tagName)

      visited.append(node.tagName)
      
      if node.tagName == "DateSeance":
        if seance_context is not None:
          output_seance_name = os.path.join(args.output, seance_context['DateSeance'][0]) + '.txt'
          print('output_seance_name', output_seance_name)
          with open(output_seance_name, 'w') as output_seance:
            output_seance.write(json.dumps(seance_context))

        seance_context = {}

  if args.debug:
    print("DEBUG:", "/".join(visited), visited)
    print("DEBUG:", " "*indent_level, str(type(node)), ":", node.toxml())

  if type(node) == Text:
    visitedFullPath = "@".join(visited)

    if args.debug_more:
        print("DEBUG:", "visitedFullPath=" + visitedFullPath, ":", node.nodeValue, )

    if any(regex.match(visitedFullPath) for regex in accepted_seance_context):
      try:
        seance_context[visited[-1:][0]].append(node.nodeValue)
      except KeyError:
        seance_context[visited[-1:][0]] = [ node.nodeValue ]
    else:
      ## Collasping childrens of "texte" such as "exposant", "italique", ...
      if len(visited) >= 2 and visited[-2] == 'texte':
        ##print("LOLILOL", visited[-2], visited[-1], seance_context[visited[-2:][0]])
        toAdd = node.nodeValue

        if visited[-1] == 'indice':
          print(visited[-1], "'{}'".format(node.nodeValue), seance_context[visited[-2:][0]][-1])

        if visited[-1] == 'exposant':
          if node.nodeValue in chars_mapping:
            toAdd = chars_mapping[node.nodeValue]
          else:
            print(visited[-1], "'{}'".format(node.nodeValue), seance_context[visited[-2:][0]][-1])

        try:
          seance_context[visited[-2:][0]][-1] += toAdd
        except KeyError:
          print("KeyError", visited, toAdd)
          ##seance_context[visited[-2:][0]][-1] = [ node.nodeValue ]

  if event == END_ELEMENT:
    indent_level -= 2
    if type(node) == Element and len(visited) > 0:
      old = visited.pop()

if args.tree_output:
  print(nx_pydot.to_pydot(structure), file=sys.stdout if args.tree_output == '-' else args.tree_output)
