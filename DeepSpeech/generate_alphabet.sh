#!/bin/bash

set -xe

pushd $HOME/ds/
	all_train_csv="$(find /mnt/extracted/data/ -type f -name '*train.csv' -printf '%p,' | sed -e 's/,$//g')"
	all_dev_csv="$(find /mnt/extracted/data/ -type f -name '*dev.csv' -printf '%p,' | sed -e 's/,$//g')"
	all_test_csv="$(find /mnt/extracted/data/ -type f -name '*test.csv' -printf '%p,' | sed -e 's/,$//g')"

	if [ ! -f "/mnt/models/alphabet.txt" ]; then
		python util/check_characters.py \
			--csv-files ${all_train_csv},${all_dev_csv},${all_test_csv} \
			--alphabet-format > /mnt/models/alphabet.txt
	fi;
popd
