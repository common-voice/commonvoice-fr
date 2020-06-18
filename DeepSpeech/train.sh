#!/bin/bash

set -xe

pushd $HOME/ds/
	all_train_csv="$(find /mnt/extracted/data/ -type f -name '*train.csv' -printf '%p,' | sed -e 's/,$//g')"
	all_dev_csv="$(find /mnt/extracted/data/ -type f -name '*dev.csv' -printf '%p,' | sed -e 's/,$//g')"
	all_test_csv="$(find /mnt/extracted/data/ -type f -name '*test.csv' -printf '%p,' | sed -e 's/,$//g')"

	mkdir -p /mnt/sources/feature_cache || true

        # Do not overwrite checkpoint file if model already exist: we will likely
	# only package
	if [ -f "/transfer-checkpoint/checkpoint" -a ! -f "/mnt/models/output_graph.pb" ]; then
		echo "Using checkpoint from ${TRANSFER_CHECKPOINT}"
		cp -a /transfer-checkpoint/* /mnt/checkpoints/
	fi;

	EARLY_STOP_FLAG="--early_stop"
	if [ "${EARLY_STOP}" = "0" ]; then
		EARLY_STOP_FLAG="--noearly_stop"
	fi;

	AMP_FLAG=""
	if [ "${AMP}" = "1" ]; then
		AMP_FLAG="--automatic_mixed_precision True"
	fi;

	# Assume that if we have best_dev_checkpoint then we have trained correctly
	if [ ! -f "/mnt/checkpoints/best_dev_checkpoint" ]; then
		python -u DeepSpeech.py \
			--show_progressbar True \
			--train_cudnn True \
			${AMP_FLAG} \
			--alphabet_config_path /mnt/models/alphabet.txt \
			--scorer_path /mnt/lm/kenlm.scorer \
			--feature_cache /mnt/sources/feature_cache \
			--train_files ${all_train_csv} \
			--dev_files ${all_dev_csv} \
			--test_files ${all_test_csv} \
			--train_batch_size ${BATCH_SIZE} \
			--dev_batch_size ${BATCH_SIZE} \
			--test_batch_size ${BATCH_SIZE} \
			--n_hidden ${N_HIDDEN} \
			--epochs ${EPOCHS} \
			--learning_rate ${LEARNING_RATE} \
			--dropout_rate ${DROPOUT} \
			--lm_alpha ${LM_ALPHA} \
			--lm_beta ${LM_BETA} \
			${EARLY_STOP_FLAG} \
			--checkpoint_dir /mnt/checkpoints/
	fi;

	python -u DeepSpeech.py \
		--show_progressbar True \
		--train_cudnn True \
		${AMP_FLAG} \
		--alphabet_config_path /mnt/models/alphabet.txt \
		--scorer_path /mnt/lm/kenlm.scorer \
		--test_files ${all_test_csv} \
		--test_batch_size ${BATCH_SIZE} \
		--n_hidden ${N_HIDDEN} \
		--lm_alpha ${LM_ALPHA} \
		--lm_beta ${LM_BETA} \
		--checkpoint_dir /mnt/checkpoints/

	if [ ! -f "/mnt/models/output_graph.pb" ]; then
		python -u DeepSpeech.py \
			--alphabet_config_path /mnt/models/alphabet.txt \
			--scorer_path /mnt/lm/kenlm.scorer \
			--feature_cache /mnt/sources/feature_cache \
			--n_hidden ${N_HIDDEN} \
			--beam_width ${BEAM_WIDTH} \
			--lm_alpha ${LM_ALPHA} \
			--lm_beta ${LM_BETA} \
			--load "best" \
			--checkpoint_dir /mnt/checkpoints/ \
			--export_dir /mnt/models/ \
			--export_language "${MODEL_EXPORT_SHORT_LANG}"
	fi;

	if [ ! -f "/mnt/models/output_graph.tflite" ]; then
		python -u DeepSpeech.py \
			--alphabet_config_path /mnt/models/alphabet.txt \
			--scorer_path /mnt/lm/kenlm.scorer \
			--feature_cache /mnt/sources/feature_cache \
			--n_hidden ${N_HIDDEN} \
			--beam_width ${BEAM_WIDTH} \
			--lm_alpha ${LM_ALPHA} \
			--lm_beta ${LM_BETA} \
			--load "best" \
			--checkpoint_dir /mnt/checkpoints/ \
			--export_dir /mnt/models/ \
			--export_tflite \
			--export_language "${MODEL_EXPORT_SHORT_LANG}"
	fi;

	if [ ! -f "/mnt/models/${MODEL_EXPORT_ZIP_LANG}.zip" ]; then
		mkdir /mnt/models/${MODEL_EXPORT_ZIP_LANG} || rm /mnt/models/${MODEL_EXPORT_ZIP_LANG}/*
		python -u DeepSpeech.py \
			--alphabet_config_path /mnt/models/alphabet.txt \
			--scorer_path /mnt/lm/kenlm.scorer \
			--feature_cache /mnt/sources/feature_cache \
			--n_hidden ${N_HIDDEN} \
			--beam_width ${BEAM_WIDTH} \
			--lm_alpha ${LM_ALPHA} \
			--lm_beta ${LM_BETA} \
			--load "best" \
			--checkpoint_dir /mnt/checkpoints/ \
			--export_dir /mnt/models/${MODEL_EXPORT_ZIP_LANG} \
			--export_zip \
			--export_language "${MODEL_EXPORT_LONG_LANG}"
	fi;

	if [ ! -f "/mnt/models/output_graph.pbmm" ]; then
		./convert_graphdef_memmapped_format --in_graph=/mnt/models/output_graph.pb --out_graph=/mnt/models/output_graph.pbmm
	fi;
popd
