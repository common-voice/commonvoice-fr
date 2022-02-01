#!/bin/bash

set -xe

pushd $HOME/ds/
	all_test_csv="$(find /mnt/extracted/data/ -type f -name '*test.csv' -printf '%p,' | sed -e 's/,$//g')"

	if [ -z "${LM_EVALUATE_RANGE}" ]; then
		echo "No language model evaluation range, skipping"
		exit 0
	fi;

	if [ ! -z "${LM_EVALUATE_RANGE}" ]; then
		LM_ALPHA_MAX="$(echo ${LM_EVALUATE_RANGE} |cut -d',' -f1)"
		LM_BETA_MAX="$(echo ${LM_EVALUATE_RANGE} |cut -d',' -f2)"
		LM_N_TRIALS="$(echo ${LM_EVALUATE_RANGE} |cut -d',' -f3)"
		
		python -u lm_optimizer.py \
			--show_progressbar True \
			--train_cudnn True \
			--alphabet_config_path /mnt/models/alphabet.txt \
			--scorer_path /mnt/lm/kenlm.scorer \
			--feature_cache /mnt/sources/feature_cache \
			--test_files ${all_test_csv} \
			--test_batch_size ${BATCH_SIZE} \
			--n_hidden ${N_HIDDEN} \
			--lm_alpha_max ${LM_ALPHA_MAX} \
			--lm_beta_max ${LM_BETA_MAX} \
			--n_trials ${LM_N_TRIALS} \
			--checkpoint_dir /mnt/checkpoints/
	fi;
popd
