#!/bin/bash

set -xe

#pushd $STT_DIR
if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
	IMPORT_AS_ENGLISH="--normalize"
fi;

if [ ! -f "/mnt/extracted/data/African_Accented_French/African_Accented_French/African_Accented_French_train.csv" ]; then
	python ${STT_DIR}/bin/import_slr57.py \
		${IMPORT_AS_ENGLISH} \
		${IMPORTERS_VALIDATE_LOCALE} \
		/mnt/extracted/data/African_Accented_French/
fi;
#opd
