#!/bin/bash

set -xe

if [ -z "${CV_RELEASE_FILENAME}" ]; then
	echo "Define a CV release"
	exit 1
fi;

pushd $HOME/ds/
	if [ ! -f "/mnt/sources/${CV_RELEASE_FILENAME}" ]; then
		exit 1
	fi;

	sha1=$(sha1sum --binary /mnt/sources/${CV_RELEASE_FILENAME} | awk '{ print $1 }')

	if [ "${sha1}" != "${CV_RELEASE_SHA256}" ]; then
		echo "Invalid Common Voice dataset"
		exit 1
	fi;

	if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
		IMPORT_AS_ENGLISH="--normalize"
	fi;

	if [ ! -f "/mnt/extracted/data/cv-${MODEL_LANGUAGE}/clips/train.csv" ]; then
		mkdir -p /mnt/extracted/data/cv-${MODEL_LANGUAGE}/ || true

		tar -C /mnt/extracted/data/cv-${MODEL_LANGUAGE}/ -xf /mnt/sources/${CV_RELEASE_FILENAME}

		if [ ${DUPLICATE_SENTENCE_COUNT} -gt 1 ]; then

			create-corpora -d /mnt/extracted/corpora -f /mnt/extracted/data/cv-${MODEL_LANGUAGE}/validated.tsv -l ${MODEL_LANGUAGE} -s ${DUPLICATE_SENTENCE_COUNT}

			mv /mnt/extracted/corpora/${MODEL_LANGUAGE}/*.tsv /mnt/extracted/data/cv-${MODEL_LANGUAGE}/

		fi;

		python bin/import_cv2.py ${IMPORT_AS_ENGLISH} /mnt/extracted/data/cv-${MODEL_LANGUAGE}/
	fi;
popd
