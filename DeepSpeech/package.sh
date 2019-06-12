#!/bin/bash

set -xe

pushd /mnt
	zip -r9 --junk-paths             \
		model_tensorflow_fr.zip  \
		models/output_graph.pbmm \
		models/alphabet.txt      \
		lm/lm.binary             \
		lm/trie

	zip -r9 --junk-paths               \
		model_tflite_fr.zip        \
		models/output_graph.tflite \
		models/alphabet.txt        \
		lm/lm.binary               \
		lm/trie
	
	all_checkpoint_path=""
	for ckpt in $(grep 'all_model_checkpoint_paths' checkpoints/checkpoint | cut -d'"' -f2);
	do
		all_checkpoint_path="${all_checkpoint_path} ${ckpt}.*"
	done;

	zip -r9 --junk-paths           \
		checkpoint_fr.zip      \
		checkpoints/checkpoint \
		${all_checkpoint_path}
popd
