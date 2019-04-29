#!/bin/sh

set -xe

export PATH=$(dirname "$0"):$PATH

checks.sh

export TMP=/mnt/tmp
export TEMP=/mnt/tmp

import_cvfr.sh

import_lingualibre.sh

import_trainingspeech.sh

generate_alphabet.sh

build_lm.sh

train_fr.sh
