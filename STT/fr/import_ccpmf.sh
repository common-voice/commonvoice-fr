#!/bin/bash

set -xe

pushd $STT_DIR
	if [ ! -f "/mnt/extracted/data/ccpmf/transcriptionsXML_audioMP3_MEFR_CCPMF_2012-2020/ccpmf_train.csv" ]; then
		#  Hot patching like that.
		sed -ri 's/MAX_SECS = .*/MAX_SECS = 4.5/g' bin/import_ccpmf.py

		python bin/import_ccpmf.py \
			${IMPORTERS_VALIDATE_LOCALE} \
			/mnt/extracted/data/ccpmf/
	fi;
popd
