#!/bin/bash

set -xe

if [ -z "${CV_RELEASE_FILENAME}" ]; then
	echo "Define a CV release"
	exit 1
fi;

pushd ${STT_DIR}
	if [ ! -f "/mnt/sources/${CV_RELEASE_FILENAME}" ]; then
		exit 1
	fi;

	sha256=$(sha256sum --binary /mnt/sources/${CV_RELEASE_FILENAME} | awk '{ print $1 }')

	if [ "${sha256}" != "${CV_RELEASE_SHA256}" ]; then
		echo "Invalid Common Voice dataset"
		exit 1
	fi;

	if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
		IMPORT_AS_ENGLISH="--normalize"
	fi;

	if [ ! -f "/mnt/extracted/data/cv-${MODEL_LANGUAGE}/clips/train.csv" ]; then
		mkdir -p /mnt/extracted/data/cv-${MODEL_LANGUAGE}/ || true

                # we don't need cv-corpus-5.1-2020-06-22/fr/, hence the strip
		tar -C /mnt/extracted/data/cv-${MODEL_LANGUAGE}/ --strip-components=2 -xf /mnt/sources/${CV_RELEASE_FILENAME}

		if [ ${DUPLICATE_SENTENCE_COUNT} -gt 1 ]; then

			create-corpora -d /mnt/extracted/corpora -f /mnt/extracted/data/cv-${MODEL_LANGUAGE}/validated.tsv -l ${MODEL_LANGUAGE} -s ${DUPLICATE_SENTENCE_COUNT}

			mv /mnt/extracted/corpora/${MODEL_LANGUAGE}/*.tsv /mnt/extracted/data/cv-${MODEL_LANGUAGE}/

		fi;

		python bin/import_cv2.py \
			${IMPORT_AS_ENGLISH} \
			${IMPORTERS_VALIDATE_LOCALE} \
			/mnt/extracted/data/cv-${MODEL_LANGUAGE}/
	fi;
popd
