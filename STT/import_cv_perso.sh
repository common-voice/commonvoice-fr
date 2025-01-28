#!/bin/bash

set -xe

if [ -z "${CV_PERSONAL_FIRST_URL}" ]; then
	echo "Not downloading your personal data from https://commonvoice.mozilla.org/"
	exit 1
fi;

if [ -z "${CV_PERSONAL_SECOND_URL}" ]; then
	echo "Not downloading your personal data from https://commonvoice.mozilla.org/"
	exit 1
fi;


pushd /mnt/sources
    CV_PERSONAL_FIRST_FILENAME=${CV_PERSONAL_FIRST_URL##*/}
    CV_PERSONAL_SECOND_FILENAME=${CV_PERSONAL_SECOND_URL##*/}

	if [ ! -f "/mnt/sources/${CV_PERSONAL_FIRST_FILENAME}" ]; then
		wget --continue $CV_PERSONAL_FIRST_URL
	fi;

    if [ ! -f "/mnt/sources/${CV_PERSONAL_SECOND_FILENAME}" ]; then
		wget --continue $CV_PERSONAL_SECOND_URL
	fi;
popd

pushd ${STT_DIR}
	
    if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
		IMPORT_AS_ENGLISH="--normalize"
	fi;

	if [ ! -f "/mnt/extracted/data/cv-${MODEL_LANGUAGE}/clips/train.csv" ]; then
		mkdir -p /mnt/extracted/data/cv-${MODEL_LANGUAGE}/ || true

		python bin/import_cv_personal.py \
			${IMPORT_AS_ENGLISH} \
			${IMPORTERS_VALIDATE_LOCALE} \
			/mnt/sources/${CV_PERSONAL_FIRST_FILENAME} \
            /mnt/sources/${CV_PERSONAL_SECOND_FILENAME}
	fi;
popd
