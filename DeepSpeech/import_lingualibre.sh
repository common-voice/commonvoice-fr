#!/bin/bash

set -xe

pushd $HOME/ds/
	if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
		IMPORT_AS_ENGLISH="--normalize"
	fi;

	if [ ! -f "/mnt/extracted/data/lingualibre/lingua_libre_Q385-ita-Italian_train.csv" ]; then
		python bin/import_lingua_libre.py                       \
			--qId 385                                        \
			--iso639-3 ita                                  \
			--english-name Italian                           \
			${IMPORT_AS_ENGLISH}                            \
			--bogus-records $HOME/lingua_libre_skiplist.txt \
			/mnt/extracted/data/lingualibre
	fi;
popd
