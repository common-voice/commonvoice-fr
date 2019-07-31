# Common Voice Data

## Table des matières

- [Introduction](#introduction)

- [Environnement](#environnement)

  - [requirements](#requirements)
  - [Installation](#installation)
  - [Mise à jour](#mise-à-jour)
  - [Execution](#execution)

- [Ressource](#ressource)

  - [Addresses](#addresses)
  - [Names](#names)
  - [XML](#xml)
  - [EPUB](#epub)
  - [TODO](#todo)

- [Testing](#testing)



# Introduction

Scripts pour extraire des contenus [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.fr "Creative Commons – CC0 1.0 universel") à destination du projet [Sentence-collector](https://common-voice.github.io/sentence-collector/) de différentes sources.

Les phrases obtenues sont composés entre 5 à 10 mots


# Environnement

## requirements

Les scripts ont été développés sous :

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


## Mise à jour

## Execution

Lors du lancement d'un terminal, vous activez l'environnement :

`$ python3 -m venv venv`

`$ . venv/bin/activate`


# Ressource

## Addresses

Address data are extracted from [source: BANO](https://www.data.gouv.fr/fr/datasets/base-d-adresses-nationale-ouverte-bano/)

Licence: ODbL

Usage: `$ python bano.py data/addresses`

see `$ python bano.py --help` for more info/options

## Names
Names data are extracted from [source: INSEE](https://www.insee.fr)

Licence: NO LICENSE

> Ils [Les fichiers détail] peuvent être téléchargés gratuitement et les données contenues dans ces fichiers peuvent être réutilisées, y compris à des fins commerciales, sans licence et sans versement de redevance, dans le cadre des mentions légales sur le site.

see https://www.insee.fr/fr/information/1300614 for more info

Usage: `$ python names.py data/names.txt`

see `$ python names.py --help` for more info/options

## XML

- <http://data.assemblee-nationale.fr/>

  - Licence ≃ CC0, avec attribution
  - Débats en XML
  - Parser qui commence à fonctionner : <https://github.com/Common-Voice/commonvoice-fr>
  - ~1.4M phrases, 35M mots, 110k mots uniques
  - ~40k mots importés sur Crowdin (20180511)


## EPUB

- [Wikisource](https://fr.wikisource.org/wiki/Wikisource:Accueil)

  - Licence: [Licence Ouverte](https://fr.wikisource.org/wiki/Licence_Ouverte)

  > Sélection : Les ouvrages sélectionnés sont des premières éditions dont le délais légales d'exploitation est dépassé

  - Usage: `$ python wikisource.py data/wikisource/epub/<auteur> data/wikisource/txt/<auteur>`
  - Example : `$ python wikisource.py data/wikisource/epub/jules-verne data/wikisource/txt/jules-verne`
  - see `$ python wikisource.py --help` for more info/options


- [source: Framabook](https://framabook.org/)

  - Licence: Différentes licences, dont certains livres en CC0
  - Usage: `$ python framabook.py data/framabook/epub/ data/framabook/txt/`
  - see `$ python framabook.py --help` for more info/options

## TODO


- <https://www.gutenberg.org/>

  - Licence domaine public
  - HTML, ePUB, Kindle et texte brut (UTF-8)
  - Parser qui commence à fonctionner : <https://github.com/Common-Voice/commonvoice-fr>
  - Premiers essais, 1 000 livres extraits au hasard sur la langue française
  - ~2,2M phrases, 42M mots, 430k mots uniques

# Testing

`$ PYTHONPATH=. pytest tests`
