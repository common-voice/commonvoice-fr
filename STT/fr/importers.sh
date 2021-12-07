#!/bin/sh

set -xe

export CV_RELEASE_FILENAME="${CV_RELEASE_FILENAME}"
export CV_RELEASE_SHA256="${CV_RELEASE_SHA256}"

../import_cv.sh

../import_lingualibre.sh

import_trainingspeech.sh

import_slr57.sh

../import_m-ailabs.sh

import_ccpmf.sh
