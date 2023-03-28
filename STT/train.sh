#!/bin/bash

set -xe

pushd ${STT_DIR}
	all_train_csv="$(find /mnt/extracted/data/ -type f -name '*train.csv' -printf '%p ' | sed -e 's/ $//g')"
	all_dev_csv="$(find /mnt/extracted/data/ -type f -name '*dev.csv' -printf '%p ' | sed -e 's/ $//g')"
	all_test_csv="$(find /mnt/extracted/data/ -type f -name '*test.csv' -printf '%p ' | sed -e 's/ $//g')"

	mkdir -p /mnt/sources/feature_cache || true

	# Do not overwrite checkpoint file if model already exist: we will likely
	# only package
	if [ -f "/transfer-checkpoint/checkpoint" -a ! -f "/mnt/models/output_graph.tflite" ]; then
		echo "Using checkpoint from ${TRANSFER_CHECKPOINT}"
		# use --load_checkpoint_dir for transfer learning
		LOAD_CHECKPOINT_FROM="--load_checkpoint_dir /transfer-checkpoint --save_checkpoint_dir /mnt/checkpoints"
	else
		LOAD_CHECKPOINT_FROM="--checkpoint_dir /mnt/checkpoints/"
	fi;

	EARLY_STOP_FLAG="--early_stop true"
	if [ "${EARLY_STOP}" = "0" ]; then
		EARLY_STOP_FLAG="--early_stop false"
	fi;

	AMP_FLAG=""
	if [ "${AMP}" = "1" ]; then
		AMP_FLAG="--automatic_mixed_precision true"
	fi;

	SKIP_BATCH_TEST_FLAG=""
	if [ "${SKIP_BATCH_TEST}" = "1" ]; then
		SKIP_BATCH_TEST_FLAG="--skip_batch_test true"
	fi;

	# Basic augmentation for data
	# TODO: Add use of overlays with noise datasets
	# ^ This would require to download and prepare noise data
	ALL_AUGMENT_FLAGS=""
	if [ "${ENABLE_AUGMENTS}" = "1" ]; then
		${$HOMEDIR}/parse_augments_args.sh
	fi;

	# Assume that if we have best_dev_checkpoint then we have trained correctly
	if [ ! -f "/mnt/checkpoints/best_dev_checkpoint" ]; then
		python -m coqui_stt_training.train \
			--show_progressbar true \
			--train_cudnn true \
			${AMP_FLAG} \
			--alphabet_config_path /mnt/models/alphabet.txt \
			--scorer_path /mnt/lm/kenlm.scorer \
			--feature_cache /mnt/sources/feature_cache \
			--train_files ${all_train_csv} \
			--dev_files ${all_dev_csv} \
			--test_files ${all_test_csv} \
			--train_batch_size ${TRAIN_BATCH_SIZE} \
			--dev_batch_size ${DEV_BATCH_SIZE} \
			--test_batch_size ${TEST_BATCH_SIZE} \
			--n_hidden ${N_HIDDEN} \
			--epochs ${EPOCHS} \
			--learning_rate ${LEARNING_RATE} \
			--dropout_rate ${DROPOUT} \
			--lm_alpha ${LM_ALPHA} \
			--lm_beta ${LM_BETA} \
			--log_level=${LOG_LEVEL} \
			${EARLY_STOP_FLAG} \
			${LOAD_CHECKPOINT_FROM} \
			${SKIP_BATCH_TEST_FLAG} \
			${ALL_AUGMENT_FLAGS}
	fi;
popd
