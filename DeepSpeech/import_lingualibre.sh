#!/bin/bash

set -xe

pushd $HOME/ds/
	if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
		IMPORT_AS_ENGLISH="--normalize"
	fi;

	if [ ! -f "/mnt/extracted/data/lingualibre/lingua_libre_Q21-fra-French_train.csv" ]; then
		python bin/import_lingua_libre.py                       \
			--qId 21                                        \
			--iso639-3 fra                                  \
			--english-name French                           \
			${IMPORT_AS_ENGLISH}                            \
			--bogus-records $HOME/lingua_libre_skiplist.txt \
			/mnt/extracted/data/lingualibre
	fi;
popd
