#!/bin/bash

set -xe

pushd ${STT_DIR}
	all_test_csv="$(find /mnt/extracted/data/ -type f -name '*test.csv' -printf '%p ' | sed -e 's/ $//g')"

	LOAD_CHECKPOINT_FROM="--checkpoint_dir /mnt/checkpoints/"

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
	ALL_METADATA_FLAGS="$ALL_METADATA_FLAGS --export_min_stt_version $METADATA_MIN_STT_VERSION"
	ALL_METADATA_FLAGS="$ALL_METADATA_FLAGS --export_max_stt_version $METADATA_MAX_STT_VERSION"
	# I never managed to use META_DESCRIPTION with STT no matter what I tried...
	#ALL_METADATA_FLAGS="$ALL_METADATA_FLAGS --export_description $METADATA_DESCRIPTION"

	if [ ! -f "/mnt/models/test_output.json" ]; then
		python -m coqui_stt_training.evaluate \
			--show_progressbar true \
			--train_cudnn true \
			${AMP_FLAG} \
			--alphabet_config_path /mnt/models/alphabet.txt \
			--scorer_path /mnt/lm/kenlm.scorer \
			--test_files ${all_test_csv} \
			--test_batch_size ${TEST_BATCH_SIZE} \
			--n_hidden ${N_HIDDEN} \
			--lm_alpha ${LM_ALPHA} \
			--lm_beta ${LM_BETA} \
			--checkpoint_dir /mnt/checkpoints/ \
			--test_output_file /mnt/models/test_output.json
	fi;

popd
