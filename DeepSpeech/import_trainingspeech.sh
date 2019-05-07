#!/bin/bash

set -xe

pushd $HOME/ds/
	pip install Unidecode==1.0.23

	if [ ! -f "/mnt/extracted/data/trainingspeech/ts_2019-04-11_fr_FR_train.csv" ]; then
		python bin/import_ts.py /mnt/extracted/data/trainingspeech
	fi;
popd
