#!/bin/bash

set -xe

#pushd $STT_DIR
if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
	IMPORT_AS_ENGLISH="--normalize"
fi;

if [ ! -f "/mnt/extracted/data/MLS/MLS_train.csv" ]; then
	python ${STT_DIR}/bin/import_mls.py \
		${IMPORT_AS_ENGLISH} \
		${IMPORTERS_VALIDATE_LOCALE} \
		-l french \
		/mnt/extracted/data/MLS/
fi;
#popd
