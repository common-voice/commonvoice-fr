#!/bin/bash

set -xe

pushd /mnt/extracted
	if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
		OLD_LANG=${LANG}
		export LANG=${LM_ICONV_LOCALE}
	fi;

	$HOMEDIR/${MODEL_LANGUAGE}/prepare_lm.sh

	if [ ! -f "sources_lm.txt" ]; then
		echo "Your language's prepare_lm.sh did not produce a sources_lm.txt file. Please fix."
		exit 1
	fi;

	if [ ! -f "/mnt/lm/kenlm.scorer" ]; then

		python $HOME/counter.py sources_lm.txt top_words.txt 500000

		lmplz	--order 4 \
			--temp_prefix /mnt/tmp/ \
			--memory 80% \
			--text sources_lm.txt \
			--arpa /mnt/lm/lm.arpa \
			--skip_symbols \
			--prune 0 0 1

		filter single model:/mnt/lm/lm.arpa /mnt/lm/lm_filtered.arpa < top_words.txt

		build_binary -a 255 \
			-q 8 \
			trie \
			/mnt/lm/lm_filtered.arpa \
			/mnt/lm/lm.binary

		pushd $HOME/ds/
			python data/lm/generate_package.py \
				--alphabet /mnt/models/alphabet.txt \
				--lm /mnt/lm/lm.binary \
				--vocab /mnt/lm/lm_filtered.arpa \
				--package /mnt/lm/kenlm.scorer \
				--default_alpha ${LM_ALPHA} \
				--default_beta ${LM_BETA}
		popd

		rm /mnt/lm/lm.arpa /mnt/lm/lm_filtered.arpa
	fi;

	if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
		export LANG=${OLD_LANG}
	fi;
popd
