#!/bin/sh

set -xe

import_cvfr.sh

import_lingualibre.sh

import_trainingspeech.sh

generate_alphabet.sh

build_lm.sh

train_fr.sh
