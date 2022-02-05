#!/bin/bash

set -xe

pushd $STT_DIR

	if [ ! -f "/mnt/extracted/data/ccpmf/transcriptionsXML_audioMP3_MEFR_CCPMF_2012-2020/ccpmf_train.csv" ]; then

		if [ "${LM_ADD_EXCLUDED_MAX_SEC}" = "1" ]; then
    	    SAVE_EXCLUDED_MAX_SEC="--save_excluded_max_sec_to_disk /mnt/extracted/data/ccpmf/ccpmf_excluded_lm.txt"
    	fi;

		#  Hot patching like that.
		sed -ri 's/MAX_SECS = .*/MAX_SECS = 4.5/g' bin/import_ccpmf.py

		python bin/import_ccpmf.py \
			${IMPORTERS_VALIDATE_LOCALE} \
			${SAVE_EXCLUDED_MAX_SEC} \
			/mnt/extracted/data/ccpmf/
	
		if [ "${LM_ADD_EXCLUDED_MAX_SEC}" = "1" ]; then
        	mv /mnt/extracted/data/ccpmf/ccpmf_excluded_lm.txt /mnt/extracted/_ccpmf_lm.txt
    	fi;
	fi;
popd
