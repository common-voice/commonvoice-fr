#!/bin/bash

set -xe

pushd $HOME/ds/
	all_test_csv="$(find /mnt/extracted/data/ -type f -name '*test.csv' -printf '%p,' | sed -e 's/,$//g')"

	if [ -z "${LM_EVALUATE_RANGE}" ]; then
		echo "No language model evaluation range, skipping"
		exit 0
	fi;

	for lm_range in ${LM_EVALUATE_RANGE}; do
		LM_ALPHA="$(echo ${lm_range} |cut -d',' -f1)"
		LM_BETA="$(echo ${lm_range} |cut -d',' -f2)"
		
		python -u evaluate.py \
			--show_progressbar True \
			--use_cudnn_rnn True \
			--alphabet_config_path /mnt/models/alphabet.txt \
			--lm_binary_path /mnt/lm/lm.binary \
			--lm_trie_path /mnt/lm/trie \
			--feature_cache /mnt/sources/feature_cache \
			--test_files ${all_test_csv} \
			--test_batch_size ${BATCH_SIZE} \
			--n_hidden ${N_HIDDEN} \
			--lm_alpha ${LM_ALPHA} \
			--lm_beta ${LM_BETA} \
			--checkpoint_dir /mnt/checkpoints/
	done;
popd
