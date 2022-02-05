#!/bin/bash

set -xe

pushd ${STT_DIR}
	if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
		IMPORT_AS_ENGLISH="--normalize"
	fi;

	if [ ! -f "/mnt/extracted/data/African_Accented_French/African_Accented_French/African_Accented_French_train.csv" ]; then
	
		if [ "${LM_ADD_EXCLUDED_MAX_SEC}" = "1" ]; then
    	    SAVE_EXCLUDED_MAX_SEC="--save_excluded_max_sec_to_disk /mnt/extracted/data/African_Accented_French/African_Accented_French_excluded_lm.txt"
	    fi;

		python bin/import_slr57.py \
			${IMPORT_AS_ENGLISH} \
			${IMPORTERS_VALIDATE_LOCALE} \
			${SAVE_EXCLUDED_MAX_SEC} \
			/mnt/extracted/data/African_Accented_French/

		if [ "${LM_ADD_EXCLUDED_MAX_SEC}" = "1" ]; then
        	mv /mnt/extracted/data/African_Accented_French/African_Accented_French_excluded_lm.txt /mnt/extracted/_slr57_lm.txt
    	fi;
	fi;
popd
