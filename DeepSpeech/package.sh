#!/bin/bash

set -xe

pushd /mnt

	if [ ! -f "model_tensorflow_fr.tar.xz" ]; then
		tar -cf - \
			-C /mnt/models/ output_graph.pbmm alphabet.txt \
			-C /mnt/lm/ kenlm.scorer | xz -T0 > model_tensorflow_fr.tar.xz
	fi;

	if [ ! -f "model_tflite_fr.tar.xz" ]; then
		tar -cf - \
			-C /mnt/models/ output_graph.tflite alphabet.txt \
			-C /mnt/lm/ kenlm.scorer | xz -T0 > model_tflite_fr.tar.xz
	fi;
	
	if [ ! -f "checkpoint_fr.tar.xz" ]; then
		all_checkpoint_path=""
		for ckpt in $(grep '^model_checkpoint_path:' checkpoints/best_dev_checkpoint | cut -d'"' -f2);
		do
			ckpt_file=$(basename "${ckpt}")
			for f in $(find checkpoints/ -type f -name "${ckpt_file}.*");
			do
				ckpt_to_add=$(basename "${f}")
				all_checkpoint_path="${all_checkpoint_path} ${ckpt_to_add}"
			done;
		done;
	
		tar -cf - \
			-C /mnt/checkpoints/ best_dev_checkpoint ${all_checkpoint_path} | xz -T0 > "checkpoint_fr.tar.xz"
	fi;

	cp /mnt/models/*.zip .
popd
