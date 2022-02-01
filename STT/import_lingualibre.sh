#!/bin/bash

set -xe

<<<<<<< HEAD
pushd $HOME/ds/
	if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
		IMPORT_AS_ENGLISH="--normalize"
	fi;

	if [ ! -f "/mnt/extracted/data/lingualibre/lingua_libre_Q${LINGUA_LIBRE_QID}-${LINGUA_LIBRE_ISO639}-${LINGUA_LIBRE_ENGLISH}_train.csv" ]; then
		if [ ! -z "${LINGUA_LIBRE_SKIPLIST}" ]; then
			SKIPLIST="--bogus-records ${LINGUA_LIBRE_SKIPLIST}"
		fi;

		python bin/import_lingua_libre.py                       \
			--qId ${LINGUA_LIBRE_QID}                       \
			--iso639-3 ${LINGUA_LIBRE_ISO639}               \
			--english-name ${LINGUA_LIBRE_ENGLISH}          \
			${IMPORT_AS_ENGLISH}                            \
			${IMPORTERS_VALIDATE_LOCALE}                    \
			${SKIPLIST}                                     \
			/mnt/extracted/data/lingualibre
	fi;
popd
=======
#pushd $STT_DIR
if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
	IMPORT_AS_ENGLISH="--normalize"
fi;

if [ ! -f "/mnt/extracted/data/lingualibre/lingua_libre_Q${LINGUA_LIBRE_QID}-${LINGUA_LIBRE_ISO639}-${LINGUA_LIBRE_ENGLISH}_train.csv" ]; then
	if [ ! -z "${LINGUA_LIBRE_SKIPLIST}" ]; then
		SKIPLIST="--bogus-records ${LINGUA_LIBRE_SKIPLIST}"
	fi;

	${VIRTUAL_ENV}/bin/python ${STT_DIR}/bin/import_lingua_libre.py                       \
		--qId ${LINGUA_LIBRE_QID}                       \
		--iso639-3 ${LINGUA_LIBRE_ISO639}               \
		--english-name ${LINGUA_LIBRE_ENGLISH}          \
		${IMPORT_AS_ENGLISH}                            \
		${IMPORTERS_VALIDATE_LOCALE}                    \
		${SKIPLIST}                                     \
		/mnt/extracted/data/lingualibre
fi;
#popd
>>>>>>> coqui-stt-1.0.0
