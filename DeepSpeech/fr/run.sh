#!/bin/sh

set -xe

${MODEL_LANGUAGE}/import_cvfr.sh

${MODEL_LANGUAGE}/import_lingualibre.sh

${MODEL_LANGUAGE}/import_trainingspeech.sh

${MODEL_LANGUAGE}/import_slr57.sh

generate_alphabet.sh

${MODEL_LANGUAGE}/build_lm.sh

${MODEL_LANGUAGE}/train.sh
