#!/bin/bash

set -xe

pushd $HOME/ds/
	if [ ! -f "/mnt/sources/it.tar.gz" ]; then
		exit 1
	fi;

	sha1=$(sha1sum --binary /mnt/sources/it.tar.gz | awk '{ print $1 }')

	if [ "${sha1}" != "2515b82b529a78c9febd5957d88dfa189ddb67e1" ]; then
		echo "Invalid Common Voice IT dataset"
		exit 1
	fi;

	if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
		IMPORT_AS_ENGLISH="--normalize"
	fi;

	if [ ! -f "/mnt/extracted/data/cv-it/clips/train.csv" ]; then
		mkdir -p /mnt/extracted/data/cv-it/ || true

		tar -C /mnt/extracted/data/cv-it/ -xf /mnt/sources/it.tar.gz

		python bin/import_cv2.py ${IMPORT_AS_ENGLISH} /mnt/extracted/data/cv-it/
	fi;
popd
