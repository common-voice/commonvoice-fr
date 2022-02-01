#!/bin/sh

set -xe

<<<<<<< HEAD
../import_cv.sh

../import_lingualibre.sh

import_trainingspeech.sh

import_slr57.sh

../import_m-ailabs.sh

import_ccpmf.sh
=======
. ${HOME}/import_cv.sh

. ${HOME}/import_lingualibre.sh

. ./import_ts.sh

. import_slr57.sh

. import_atthack.sh

. import_mls.sh

. ${HOME}/import_m-ailabs.sh

#. ./import_ccpmf.sh
>>>>>>> coqui-stt-1.0.0
