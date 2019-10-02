#!/bin/bash

set -xe

pushd $HOME/ds/
	if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
		IMPORT_AS_ENGLISH="--normalize"
	fi;

	if [ ! -f "/mnt/extracted/data/African_Accented_French/African_Accented_French/African_Accented_French_train.csv" ]; then
		python bin/import_slr57.py ${IMPORT_AS_ENGLISH} /mnt/extracted/data/African_Accented_French/
	fi;
popd
