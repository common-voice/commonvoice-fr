#!/bin/bash

set -xe

pushd $STT_DIR
	if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
		IMPORT_AS_ENGLISH="--normalize"
	fi;

	if [ ! -f "/mnt/extracted/data/M-AILABS/${M_AILABS_LANG}/${M_AILABS_LANG}_train.csv" ]; then
		
		if [ "${LM_ADD_EXCLUDED_MAX_SEC}" = "1" ]; then
        	SAVE_EXCLUDED_MAX_SEC="--save_excluded_max_sec_to_disk /mnt/extracted/data/M-AILABS/M-AILABS_excluded_lm.txt"
    	fi;

		if [ ! -z "${M_AILABS_SKIP}" ]; then
			SKIPLIST="--skiplist ${M_AILABS_SKIP}"
		fi;

		python bin/import_m-ailabs.py ${IMPORT_AS_ENGLISH}      \
			${SKIPLIST}                                     \
			--language ${M_AILABS_LANG}                     \
			${IMPORTERS_VALIDATE_LOCALE}                    \
			${SAVE_EXCLUDED_MAX_SEC} \
			/mnt/extracted/data/M-AILABS/

		if [ "${LM_ADD_EXCLUDED_MAX_SEC}" = "1" ]; then
    	    mv /mnt/extracted/data/M-AILABS/M-AILABS_excluded_lm.txt /mnt/extracted/_m-ailabs_lm.txt
	    fi;
	fi;
popd
