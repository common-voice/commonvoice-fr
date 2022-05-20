#!/bin/sh

set -xe

export IMPORTERS_VALIDATE_LOCALE="--validate_label_locale $HOME/${MODEL_LANGUAGE}/validate_label.py"

export CV_RELEASE_FILENAME="cv-corpus-9.0-2022-04-27-fr.tar.gz"
export CV_RELEASE_SHA256="6e5326e0cd1841ed3e5fceeb46e71d39c1cb653968f0e888c62d0369cc06cb9d"

export LINGUA_LIBRE_QID="21"
export LINGUA_LIBRE_ISO639="fra"
export LINGUA_LIBRE_ENGLISH="French"
export LINGUA_LIBRE_SKIPLIST="$HOME/${MODEL_LANGUAGE}/lingua_libre_skiplist.txt"

export M_AILABS_LANG="fr_FR"
export M_AILABS_SKIP="monsieur_lecoq,les_mysteres_de_paris"

export LM_ICONV_LOCALE="fr_FR.UTF-8"

export MODEL_EXPORT_ZIP_LANG="fr-fr"
