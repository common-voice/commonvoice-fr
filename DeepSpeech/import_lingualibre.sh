#!/bin/bash

set -xe

pushd $HOME/ds/
	if [ ! -f "/mnt/extracted/data/lingualibre/lingua_libre_Q21-fra-French_train.csv" ]; then
		python bin/import_lingua_libre.py \
			--qId 21                  \
			--iso639-3 fra            \
			--english-name French     \
			/mnt/extracted/data/lingualibre
	fi;
popd
