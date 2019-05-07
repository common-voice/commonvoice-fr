#!/bin/bash

set -xe

pushd /mnt/extracted
	if [ ! -f "wiki_fr_lower.txt" ]; then
		curl -sSL https://github.com/Common-Voice/commonvoice-fr/releases/download/lm-0.1/wiki.txt.xz | pixz -d | tr '[:upper:]' '[:lower:]' > wiki_fr_lower.txt
	fi;

	if [ ! -f "/mnt/lm/lm.binary" ]; then
		lmplz	--order 3 \
			--temp_prefix /mnt/tmp/ \
			--memory 80% \
			--text wiki_fr_lower.txt \
			--arpa /mnt/lm/lm.arpa \
			--skip_symbols \
			--prune 0 1

		build_binary -a 255 \
			-q 8 \
			trie \
			/mnt/lm/lm.arpa \
			/mnt/lm/lm.binary

		rm /mnt/lm/lm.arpa
		> wiki_fr_lower.txt
	fi;

	if [ ! -f "/mnt/lm/trie" ]; then
		curl -sSL https://index.taskcluster.net/v1/task/project.deepspeech.deepspeech.native_client.master.${DS_BRANCH}.cpu/artifacts/public/native_client.tar.xz | pixz -d | tar -xf -
		./generate_trie /mnt/models/alphabet.txt /mnt/lm/lm.binary /mnt/lm/trie
	fi;
popd
