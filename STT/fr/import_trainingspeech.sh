#!/bin/bash

set -xe

pushd ${STT_DIR}
	pip install Unidecode==1.0.23

	if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
		IMPORT_AS_ENGLISH="--english-compatible"
	fi;

	if [ ! -f "/mnt/extracted/data/trainingspeech/ts_2019-04-11_fr_FR_train.csv" ]; then
		python bin/import_ts.py \
			${IMPORT_AS_ENGLISH} \
			${IMPORTERS_VALIDATE_LOCALE} \
			/mnt/extracted/data/trainingspeech
	fi;
popd
