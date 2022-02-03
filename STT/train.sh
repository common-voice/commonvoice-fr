#!/bin/bash

set -xe

pushd $STT_DIR
	all_train_csv="$(find /mnt/extracted/data/ -type f -name '*train.csv' -printf '%p ' | sed -e 's/ $//g')"
	all_dev_csv="$(find /mnt/extracted/data/ -type f -name '*dev.csv' -printf '%p ' | sed -e 's/ $//g')"
	all_test_csv="$(find /mnt/extracted/data/ -type f -name '*test.csv' -printf '%p ' | sed -e 's/ $//g')"

	mkdir -p /mnt/sources/feature_cache || true

        # Do not overwrite checkpoint file if model already exist: we will likely
	# only package
	if [ -f "/transfer-checkpoint/checkpoint" -a ! -f "/mnt/models/output_graph.pb" ]; then
		echo "Using checkpoint from ${TRANSFER_CHECKPOINT}"
		cp -a /transfer-checkpoint/* /mnt/checkpoints/
	fi;

	EARLY_STOP_FLAG="--early_stop true"
	if [ "${EARLY_STOP}" = "0" ]; then
		EARLY_STOP_FLAG="--early_stop false"
	fi;

	AMP_FLAG=""
	if [ "${AMP}" = "1" ]; then
		AMP_FLAG="--automatic_mixed_precision True"
	fi;

	# Check metadata existence
	if [ -z "$METADATA_AUTHOR" ]; then
		echo "Please fill-in metadata informations"
		exit 1
	fi;

	# Ok, assume we have all the metadata now
	ALL_METADATA_FLAGS="--export_author_id $METADATA_AUTHOR"
	ALL_METADATA_FLAGS="$ALL_METADATA_FLAGS --export_model_version $METADATA_MODEL_VERSION"
	ALL_METADATA_FLAGS="$ALL_METADATA_FLAGS --export_contact_info $METADATA_CONTACT_INFO"
	ALL_METADATA_FLAGS="$ALL_METADATA_FLAGS --export_license $METADATA_LICENSE"
	ALL_METADATA_FLAGS="$ALL_METADATA_FLAGS --export_language $METADATA_LANGUAGE"
	ALL_METADATA_FLAGS="$ALL_METADATA_FLAGS --export_min_stt_version $METADATA_MIN_DS_VERSION"
	ALL_METADATA_FLAGS="$ALL_METADATA_FLAGS --export_max_stt_version $METADATA_MAX_DS_VERSION"
	#ALL_METADATA_FLAGS="$ALL_METADATA_FLAGS --export_description $METADATA_DESCRIPTION"

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

	if [ ! -f "/mnt/models/test_output.json" ]; then
		python -m coqui_stt_training.evaluate \
			--show_progressbar true \
			--train_cudnn true \
			${AMP_FLAG} \
			--alphabet_config_path /mnt/models/alphabet.txt \
			--scorer_path /mnt/lm/kenlm.scorer \
			--test_files ${all_test_csv} \
			--test_batch_size ${BATCH_SIZE} \
			--n_hidden ${N_HIDDEN} \
			--lm_alpha ${LM_ALPHA} \
			--lm_beta ${LM_BETA} \
			--checkpoint_dir /mnt/checkpoints/ \
			--test_output_file /mnt/models/test_output.json
	fi;

	if [ ! -f "/mnt/models/output_graph.tflite" ]; then
		METADATA_MODEL_NAME_FLAG="--export_model_name $METADATA_MODEL_NAME-tflite"
		python -m coqui_stt_training.export \
			--alphabet_config_path /mnt/models/alphabet.txt \
			--scorer_path /mnt/lm/kenlm.scorer \
			--feature_cache /mnt/sources/feature_cache \
			--n_hidden ${N_HIDDEN} \
			--beam_width ${BEAM_WIDTH} \
			--lm_alpha ${LM_ALPHA} \
			--lm_beta ${LM_BETA} \
			--load_evaluate "best" \
			--checkpoint_dir /mnt/checkpoints/ \
			--export_dir /mnt/models/ \
			--export_tflite true \
			${ALL_METADATA_FLAGS} \
			${METADATA_MODEL_NAME_FLAG}
	fi;

	if [ ! -f "/mnt/models/${MODEL_EXPORT_ZIP_LANG}.zip" ]; then
		mkdir /mnt/models/${MODEL_EXPORT_ZIP_LANG} || rm /mnt/models/${MODEL_EXPORT_ZIP_LANG}/*
		METADATA_MODEL_NAME_FLAG="--export_model_name $METADATA_MODEL_NAME-tflite"
		python -m coqui_stt_training.export \
			--alphabet_config_path /mnt/models/alphabet.txt \
			--scorer_path /mnt/lm/kenlm.scorer \
			--feature_cache /mnt/sources/feature_cache \
			--n_hidden ${N_HIDDEN} \
			--beam_width ${BEAM_WIDTH} \
			--lm_alpha ${LM_ALPHA} \
			--lm_beta ${LM_BETA} \
			--load_evaluate "best" \
			--checkpoint_dir /mnt/checkpoints/ \
			--export_dir /mnt/models/${MODEL_EXPORT_ZIP_LANG} \
			--export_zip true \
			${ALL_METADATA_FLAGS} \
			${METADATA_MODEL_NAME_FLAG}
	fi;
popd
