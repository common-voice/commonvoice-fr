#!/bin/sh

set -xe

export IMPORTERS_VALIDATE_LOCALE="--validate_label_locale $HOME/${MODEL_LANGUAGE}/validate_label.py"

export CV_RELEASE_FILENAME="cv-corpus-12.0-2022-12-07-fr.tar.gz"
export CV_RELEASE_SHA256="00afc519d48d749a4724386dc203b8a0286060efe4ccb46963555794fef216eb"

export LINGUA_LIBRE_QID="21"
export LINGUA_LIBRE_ISO639="fra"
export LINGUA_LIBRE_ENGLISH="French"
export LINGUA_LIBRE_SKIPLIST="$HOME/${MODEL_LANGUAGE}/lingua_libre_skiplist.txt"

export M_AILABS_LANG="fr_FR"
export M_AILABS_SKIP="monsieur_lecoq,les_mysteres_de_paris"

export LM_ICONV_LOCALE="fr_FR.UTF-8"

export MODEL_EXPORT_ZIP_LANG="fr-fr"
