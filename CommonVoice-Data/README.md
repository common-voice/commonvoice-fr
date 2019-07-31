# Groupe de travail pour Common Voice en français

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

  - [EPUB](#epub)

  - [Testing](#testing)



# Introduction

Extraction de contenu en [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.fr "Creative Commons – CC0 1.0 universel") à destination du projet [Sentence-collector]()


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


## EPUB

### Framabook

Address data are extracted from [source: Framabook](https://framabook.org/)

Licence: CCO (pour certains livres)

Usage: `$ python framabook.py data/framabook/epub/ data/framabook/txt/`

see `$ python framabook.py --help` for more info/options



## Testing
`$ PYTHONPATH=. pytest tests`
