#!/usr/bin/env python3

import sys
from xml.dom.pulldom import START_ELEMENT, CHARACTERS, END_ELEMENT, parse
from xml.dom.minidom import Element, Text

doc = parse(sys.argv[1])
indent_level = 0
visited = []

is_syceron = False

accepted_seance_context = [
  "CompteRendu|Metadonnees|DateSeance",
  "CompteRendu|Metadonnees|Sommaire|Sommaire1|TitreStruct|Intitule",
  "CompteRendu|Contenu|Quantiemes|Journee",
  "CompteRendu|Contenu|ouverture_seance|paragraphe|ORATEURS|ORATEUR|NOM",
  "CompteRendu|Contenu|ouverture_seance|paragraphe|texte",
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

  if type(node) == Text:
    #print("/".join(visited))
    #print(" "*indent_level, str(type(node)), ":", node.toxml())
    visitedFullPath = "|".join(visited)
    #print(visitedFullPath, ":", node.nodeValue)

    if visitedFullPath in accepted_seance_context:
      seance_context[visited[-1:][0]] = node.nodeValue

  if event == END_ELEMENT:
    indent_level -= 2
    if type(node) == Element and len(visited) > 0:
      old = visited.pop()
