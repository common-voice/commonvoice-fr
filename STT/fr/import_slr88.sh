#!/bin/bash

set -xe

#pushd $STT_DIR
if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
	IMPORT_AS_ENGLISH="--normalize"
fi;

if [ ! -f "/mnt/extracted/data/Att-HACK/Att-HACK_train.csv" ]; then
	python ${STT_DIR}/bin/import_slr88.py \
		${IMPORT_AS_ENGLISH} \
		${IMPORTERS_VALIDATE_LOCALE} \
		/mnt/extracted/data/Att-HACK/
fi;
#opd
