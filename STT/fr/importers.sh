#!/bin/sh

set -xe

. ${HOME}/import_cv.sh

. ${HOME}/import_lingualibre.sh

. ./import_trainingspeech.sh

. import_slr57.sh

. ${HOME}/import_m-ailabs.sh

. ./import_ccpmf.sh
