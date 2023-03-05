#!/bin/bash

set -xe

pushd ${STT_DIR}
	all_test_csv="$(find /mnt/extracted/data/ -type f -name '*test.csv' -printf '%p ' | sed -e 's/ $//g')"

	LOAD_CHECKPOINT_FROM="--checkpoint_dir /mnt/checkpoints/"

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

	if [ ! -f "/mnt/models/output_graph.tflite" ]; then
		METADATA_MODEL_NAME_FLAG="--export_model_name $METADATA_MODEL_NAME-tflite"
		${HOME}/tf-venv/bin/python -m coqui_stt_training.export \
			--alphabet_config_path /mnt/models/alphabet.txt \
			--scorer_path /mnt/lm/kenlm.scorer \
			--feature_cache /mnt/sources/feature_cache \
			--n_hidden ${N_HIDDEN} \
			--beam_width ${BEAM_WIDTH} \
			--lm_alpha ${LM_ALPHA} \
			--lm_beta ${LM_BETA} \
			--load_evaluate "best" \
			${LOAD_CHECKPOINT_FROM} \
			--export_dir /mnt/models/ \
			--export_tflite true \
			${ALL_METADATA_FLAGS} \
			${METADATA_MODEL_NAME_FLAG}
	fi;

	if [ ! -f "/mnt/models/${MODEL_EXPORT_ZIP_LANG}.zip" ]; then
		mkdir /mnt/models/${MODEL_EXPORT_ZIP_LANG} || rm /mnt/models/${MODEL_EXPORT_ZIP_LANG}/*
		METADATA_MODEL_NAME_FLAG="--export_model_name $METADATA_MODEL_NAME-tflite"
		${HOME}/tf-venv/bin/python -m coqui_stt_training.export \
			--alphabet_config_path /mnt/models/alphabet.txt \
			--scorer_path /mnt/lm/kenlm.scorer \
			--feature_cache /mnt/sources/feature_cache \
			--n_hidden ${N_HIDDEN} \
			--beam_width ${BEAM_WIDTH} \
			--lm_alpha ${LM_ALPHA} \
			--lm_beta ${LM_BETA} \
			--load_evaluate "best" \
			${LOAD_CHECKPOINT_FROM} \
			--export_dir /mnt/models/${MODEL_EXPORT_ZIP_LANG} \
			--export_zip true \
			${ALL_METADATA_FLAGS} \
			${METADATA_MODEL_NAME_FLAG}
	fi;
popd
