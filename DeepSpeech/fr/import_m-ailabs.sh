#!/bin/bash

set -xe

pushd $HOME/ds/
	if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
		IMPORT_AS_ENGLISH="--normalize"
	fi;

	if [ ! -f "/mnt/extracted/data/M-AILABS/fr_FR/fr_FR_train.csv" ]; then
		python bin/import_m-ailabs.py ${IMPORT_AS_ENGLISH}      \
			--skiplist monsieur_lecoq,les_mysteres_de_paris \
			--language fr_FR                                \
			/mnt/extracted/data/M-AILABS/
	fi;
popd
