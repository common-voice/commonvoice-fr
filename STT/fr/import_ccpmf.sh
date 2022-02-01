#!/bin/bash

set -xe

<<<<<<< HEAD
pushd $HOME/ds/
	if [ ! -f "/mnt/extracted/data/ccpmf/transcriptionsXML_audioMP3_MEFR_CCPMF_2012-2020/ccpmf_train.csv" ]; then
		#  Hot patching like that.
		sed -ri 's/MAX_SECS = .*/MAX_SECS = 4.5/g' bin/import_ccpmf.py

		python bin/import_ccpmf.py \
			${IMPORTERS_VALIDATE_LOCALE} \
			/mnt/extracted/data/ccpmf/
	fi;
popd
=======
#pushd $STT_DIR
if [ ! -f "/mnt/extracted/data/ccpmf/transcriptionsXML_audioMP3_MEFR_CCPMF_2012-2020/ccpmf_train.csv" ]; then
	#  Hot patching like that.
	sed -ri 's/MAX_SECS = .*/MAX_SECS = 4.5/g' ${STT_DIR}/bin/import_ccpmf.py

	python ${STT_DIR}/bin/import_ccpmf.py \
		${IMPORTERS_VALIDATE_LOCALE} \
		--normalize \
		/mnt/extracted/data/ccpmf/
fi;
#popd
>>>>>>> coqui-stt-1.0.0
