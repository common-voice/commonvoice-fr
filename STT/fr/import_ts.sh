#!/bin/bash

set -xe

#pushd $STT_DIR
#pip install Unidecode==1.0.23

if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
	IMPORT_AS_ENGLISH="--english-compatible"
fi;

if [ ! -f "/mnt/extracted/data/TrainingSpeech/ts_2019-04-11_fr_FR_train.csv" ]; then
	python ${STT_DIR}/bin/import_ts.py \
		${IMPORT_AS_ENGLISH} \
		${IMPORTERS_VALIDATE_LOCALE} \
		/mnt/extracted/data/TrainingSpeech
fi;
#popd
