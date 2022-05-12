#!/bin/sh

set -xe

../import_cv.sh

../import_lingualibre.sh

import_trainingspeech.sh

import_slr57.sh

../import_m-ailabs.sh

./import_atthack.sh

./import_mls.sh

#./import_ccpmf.sh
