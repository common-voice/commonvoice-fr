#!/bin/bash

set -xe

pushd ${STT_DIR}
	all_train_csv="$(find /mnt/extracted/data/ -type f -name '*train.csv' -printf '%p,' | sed -e 's/,$//g')"
	all_dev_csv="$(find /mnt/extracted/data/ -type f -name '*dev.csv' -printf '%p,' | sed -e 's/,$//g')"
	all_test_csv="$(find /mnt/extracted/data/ -type f -name '*test.csv' -printf '%p,' | sed -e 's/,$//g')"

	if [ ! -f "/mnt/models/alphabet.txt" ]; then
		if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
			cp data/alphabet.txt /mnt/models/alphabet.txt
		else
			python -m coqui_stt_training.util.check_characters \
				--csv-files ${all_train_csv},${all_dev_csv},${all_test_csv} \
				--alphabet-format | grep -v '^#' | sort -n > /mnt/models/alphabet.txt
		fi;
	fi;
popd
