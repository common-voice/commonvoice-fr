#!/usr/bin/env python3

import sys
import re
from xml.dom.pulldom import START_ELEMENT, CHARACTERS, END_ELEMENT, parse
from xml.dom.minidom import Element, Text

doc = parse(sys.argv[1])
debug = len(sys.argv) == 3 and sys.argv[2] == "--debug"
debug_more = len(sys.argv) == 3 and sys.argv[2] == "--debug-more"
indent_level = 0
visited = []

is_syceron = False

accepted_seance_context = [
  re.compile("CompteRendu@Metadonnees@DateSeance"),
  re.compile("CompteRendu@Metadonnees@Sommaire@Sommaire1@TitreStruct@Intitule"),
  re.compile("CompteRendu@Contenu@Quantiemes@Journee"),
  re.compile("CompteRendu@Contenu@ouverture_seance@paragraphe@ORATEURS@ORATEUR@NOM"),
  re.compile(".*@paragraphe@texte.*"),
]
seance_context = None

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
      visited.append(node.tagName)
      
      if node.tagName == "DateSeance":
        print(seance_context)
        seance_context = {}

  if debug:
    print("DEBUG:", "/".join(visited), visited)
    print("DEBUG:", " "*indent_level, str(type(node)), ":", node.toxml())

  if type(node) == Text:
    visitedFullPath = "@".join(visited)

    if debug_more:
        print("DEBUG:", "visitedFullPath=" + visitedFullPath, ":", node.nodeValue, )

    if any(regex.match(visitedFullPath) for regex in accepted_seance_context):
      try:
        seance_context[visited[-1:][0]] += " " + node.nodeValue
      except KeyError:
        seance_context[visited[-1:][0]] = node.nodeValue

  if event == END_ELEMENT:
    indent_level -= 2
    if type(node) == Element and len(visited) > 0:
      old = visited.pop()
