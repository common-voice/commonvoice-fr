#!/bin/bash

set -xe

pushd $HOME/ds/
	CV_FR="cv-3-fr.tar.gz"

	if [ ! -f "/mnt/sources/cv-3-fr.tar.gz" ]; then
		exit 1
	fi;

	sha1=$(sha1sum --binary /mnt/sources/cv-3-fr.tar.gz | awk '{ print $1 }')

	if [ "${sha1}" != "5ba6967d08aee255a36b2a8087cf638e499d163f" ]; then
		echo "Invalid Common Voice FR v3 dataset"
		exit 1
	fi;

	if [ "${ENGLISH_COMPATIBLE}" = "1" ] ; then
		IMPORT_AS_ENGLISH="--normalize"
	fi;

	if [ ! -f "/mnt/extracted/data/cv-fr/clips/train.csv" ]; then
		mkdir -p /mnt/extracted/data/cv-fr/ || true

		tar -C /mnt/extracted/data/cv-fr/ -xf /mnt/sources/cv-3-fr.tar.gz

		if [ ${DUPLICATE_SENTENCE_COUNT} -gt 1 ]; then

			create-corpora -d /mnt/extracted/corpora -f /mnt/extracted/data/cv-fr/validated.tsv -l fr -s ${DUPLICATE_SENTENCE_COUNT}

			mv /mnt/extracted/corpora/fr/*.tsv /mnt/extracted/data/cv-fr/

		fi;

		# Allow overwriting TSVs files before importing, for hacking with Corpora Creator
		if [ -f "/mnt/sources/cv-fr-overwrite.tar.gz" ]; then
			tar -C /mnt/extracted/data/cv-fr/ -xf /mnt/sources/cv-fr-overwrite.tar.gz
		fi;

		python bin/import_cv2.py ${IMPORT_AS_ENGLISH} /mnt/extracted/data/cv-fr/
	fi;
popd
