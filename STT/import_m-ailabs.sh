#!/bin/bash

set -xe

#pushd $STT_DIR
if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
	IMPORT_AS_ENGLISH="--normalize"
fi;

if [ ! -f "/mnt/extracted/data/M-AILABS/${M_AILABS_LANG}/${M_AILABS_LANG}_train.csv" ]; then
	if [ ! -z "${M_AILABS_SKIP}" ]; then
		SKIPLIST="--skiplist ${M_AILABS_SKIP}"
	fi;

	python ${STT_DIR}bin/import_m-ailabs.py ${IMPORT_AS_ENGLISH}      \
		${SKIPLIST}                                     \
		--language ${M_AILABS_LANG}                     \
		${IMPORTERS_VALIDATE_LOCALE}                    \
		/mnt/extracted/data/M-AILABS/
fi;
#popd
