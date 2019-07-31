# Common Voice Data

## Table des matières

- [Introduction](#introduction)

- [Environnement](#environnement)

  - [Prérequis](#prérequis)
  - [Installation](#installation)
  - [Execution](#execution)

- [Ressources](#ressources)

  - [CSV](#csv)
  - [TXT](#txt)
  - [XML](#xml)
  - [JSON](#json)
  - [EPUB](#epub)

- [TODO](#todo)

- [Testing](#testing)

# Introduction

Scripts permettant d'extraire des contenus en [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.fr "Creative Commons – CC0 1.0 universel") à destination du projet [Sentence-collector](https://common-voice.github.io/sentence-collector/) sous différents formats.

Les phrases obtenues sont composées de 5 à 10 mots et pourront être ajoutées à <https://common-voice.github.io/sentence-collector/#/add>

# Environnement

## Prérequis

Les scripts ont été développés sous :

- Linux

- python>=3.6

## Installation

Installation d'un nouvel environnement dans le dossier DATA

`$ git clone.....`

`$ cd CommonVoice-Data`

`$ python3 -m venv venv`

`$ . venv/bin/activate`

`$ python -m spacy download fr_core_news_sm`

`$ pip install -r requirements.txt`

## Exécution

Lors du lancement d'un terminal, vous activez l'environnement :

`$ python3 -m venv venv`

`$ . venv/bin/activate`

# Ressources

## CSV

- [BANO](https://www.data.gouv.fr/fr/datasets/base-d-adresses-nationale-ouverte-bano/)

  - Address data are extracted from
  - Licence : ODbL
  - Usage : `$ python bano.py data/addresses`
  - see `$ python bano.py --help` for more info/options

## TXT

- [Gutenberg](https://www.gutenberg.org/)

  - Licence domaine public
  - HTML, ePUB, Kindle et texte brut (UTF-8)
  - Parser qui commence à fonctionner : <https://github.com/Common-Voice/commonvoice-fr>
  - Premiers essais, 1 000 livres extraits au hasard sur la langue française
  - ~2,2M phrases, 42M mots, 430k mots uniques
  - Usage : `$ python project-gutenberg.py`

- [INSEE](https://www.insee.fr)

  - Licence: NO LICENSE

  > Ils [Les fichiers détail] peuvent être téléchargés gratuitement et les données contenues dans ces fichiers peuvent être réutilisées, y compris à des fins commerciales, sans licence et sans versement de redevance, dans le cadre des mentions légales sur le site.

  - see https://www.insee.fr/fr/information/1300614 for more info
  - Usage: `$ python names.py data/insee/names.txt`
  - see `$ python names.py --help` for more info/options

- [libre théatre](http://libretheatre.fr/)

    - Licence : domaine public
    - Format : HTML, texte brut (UTF-8)
    - Parser en cours <https://github.com/Common-Voice/commonvoice-fr>

## XML

- [Assemblée nationale](http://data.assemblee-nationale.fr/)

  - Licence ≃ CC0, avec attribution
  - Débats en XML
  - Parser qui commence à fonctionner : <https://github.com/Common-Voice/commonvoice-fr>
  - ~1.4M phrases, 35M mots, 110k mots uniques
  - ~40k mots importés sur Crowdin (20180511)

## JSON

- [Wikipédia](https://fr.wikipedia.org)

  - Licence
  - Contenu : échantillons de phrases de quelques pages

## EPUB

Documentation [EPUB](https://buildmedia.readthedocs.org/media/pdf/ebooklib/latest/ebooklib.pdf)

- [Wikisource](https://fr.wikisource.org/wiki/Wikisource:Accueil)

  - Licence : [Licence Ouverte](https://fr.wikisource.org/wiki/Licence_Ouverte)

  > Sélection : les ouvrages sélectionnés sont des premières éditions dont le délai légal du monopole d'exploitation est dépassé

  - Usage : `$ python wikisource.py data/wikisource/epub/<auteur> data/wikisource/txt/<auteur>`
  - Example : `$ python wikisource.py data/wikisource/epub/jules-verne data/wikisource/txt/jules-verne`
  - see `$ python wikisource.py --help` for more info/options

- [Framabook](https://framabook.org/)

  - Licence  : différentes licences, dont certains livres en CC0
  - Usage : `$ python framabook.py data/framabook/epub/ data/framabook/txt/`
  - see `$ python framabook.py --help` for more info/options

# TODO

Il a été identifié des sites internet à parser :

  - <http://www.cuisine-libre.fr/>

    - Licence domaine public
    - HTML, texte brut (UTF-8)
    - À PARSER

  - <http://www.inlibroveritas.net/>

    - [Licence Art Libre – LAL 1.3](http://artlibre.org/licence/lal)
    - **PDF À PARSER**

# Testing

`$ PYTHONPATH=. pytest tests`
