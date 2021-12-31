#!/bin/sh

set -xe

. ${HOME}/import_cv.sh

. ${HOME}/import_lingualibre.sh

#. ./import_mswc.sh # STT/bin/import_mswc.py doesn't work for now

. import_slr57.sh

. import_slr88.sh

. ${HOME}/import_m-ailabs.sh

. ./import_ccpmf.sh
