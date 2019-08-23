# Common Voice Data

## Table of Contents

- [Introduction](#introduction)

- [Environment](#environment)

  - [Configuration](#Configuration)
  - [Installation](#installation)
  - [Execution](#execution)
  - [Close](#Close)

- [Resources](#resources)

  - [CSV](#csv)
  - [TXT](#txt)
  - [XML](#xml)
  - [JSON](#json)
  - [EPUB](#epub)

- [Testing](#testing)

# Introduction

Scripts to extract content in [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.fr "Creative Commons – CC0 1.0 universel") for the   [Sentence-collector](https://common-voice.github.io/sentence-collector/) project in different format.

The sentences obtained are composed of 3 to 14 words and can be added at  <https://common-voice.github.io/sentence-collector/#/add>

# Environment

## Configuration

The scripts were tested under:

- Linux

- python>=3.6

## Installation

Installing a new environment in the DATA folder

```
git clone git@github.com:Common-Voice/commonvoice-fr.git
cd CommonVoice-Data
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```


if you get the following message :
```
  Can't find a local Berkeley DB installation
```
you must do this :

```
sudo apt-get install libdb-dev
brew install berkeley-db
```


## Execution

When launching a terminal, you activate the environment:

```
cd CommonVoice-Data
. venv/bin/activate
```


## Close

if you want to stop the environment, you deactivate the environment:

```
deactivate
```


# Resources

## CSV

- [BANO](https://www.data.gouv.fr/fr/datasets/base-d-adresses-nationale-ouverte-bano/)

  - Address data are extracted from
  - Licence: ODbL
  - Usage: `$ python bano.py data/addresses`
  - see: `$ python bano.py --help` for more info/options

## TXT

- [Gutenberg](https://www.gutenberg.org/)

  - Licence: public domain
  - 1,000 books randomly extracted on the French language
  - ~2,2M sentences, 42M words, 430k unique words
  - Usage : `$ python project-gutenberg.py`

- [INSEE](https://www.insee.fr)

  - Licence: NO LICENSE

  > They [The detail files] may be downloaded free of charge and the data contained in these files may be reused, including for commercial purposes, without licence and without payment of royalties, as part of the legal notices on the site.

  - see https://www.insee.fr/fr/information/1300614 for more info
  - Usage: `$ python names.py data/insee/names.txt`
  - see `$ python names.py --help` for more info/options


- [libre theatre](http://libretheatre.fr/)

    - Licence: public domain
    - Format: HTML, plain text (UTF-8)
    - Usage: `$ python libretheatre.py`
    - see: `$ python libretheatre.py --help` for more info/options


## XML

- [Assemblée nationale](http://data.assemblee-nationale.fr/)

  - Licence: CC0, with attribution
  - Débates in XML
  - ~1.4M sentences, 35M words, 110k unique words
  - Format : HTML, plain text (UTF-8)
  - Usage: `$ debats-assemblee-nationale.sh`

## JSON

- [Wikipédia](https://fr.wikipedia.org)

  - Licence:
  - Content: Sample sentences of a few pages
  - Usage: `$ python wikipedia.py`

## EPUB

Documentation [EPUB](https://buildmedia.readthedocs.org/media/pdf/ebooklib/latest/ebooklib.pdf)

- [Wikisource](https://fr.wikisource.org/wiki/Wikisource:Accueil)

  - Licence: [Open License](https://fr.wikisource.org/wiki/Licence_Ouverte)

  > Selection: the selected works are first editions whose legal time limit for the operating monopoly has been exceeded

  - see: `$ python wikisource.py --help` for more info/options
  - Usage 1: `$ python wikisource.py -1 data/wikisource/txt/<author>`
  - Example 1: `$ python wikisource.py -1 data/wikisource/txt/jules-verne`

  - Usage 2: `$ python wikisource.py data/wikisource/epub/<author> data/wikisource/txt/<author>`
  - Example 2: `$ python wikisource.py data/wikisource/epub/jules-verne data/wikisource/txt/jules-verne`

- [Framabook](https://framabook.org/)

  - License: various licenses, including some CC0 books
  - Usage : `$ python framabook.py data/framabook/epub/ data/framabook/txt/`
  - see: `$ python framabook.py --help` for more info/options



# Testing

`$ PYTHONPATH=. pytest tests`
