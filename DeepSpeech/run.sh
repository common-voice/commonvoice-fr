#!/bin/sh

set -xe

THIS=$(dirname "$0")
export PATH=${THIS}:${THIS}/${MODEL_LANGUAGE}:$PATH

export TF_CUDNN_RESET_RND_GEN_STATE=1

env

checks.sh

export TMP=/mnt/tmp
export TEMP=/mnt/tmp

. params.sh
. ${MODEL_LANGUAGE}/params.sh

if [ -x "${MODEL_LANGUAGE}/metadata.sh" ]; then
	. ${MODEL_LANGUAGE}/metadata.sh
else
	echo "Please prepare metadata informations."
	exit 1
fi;

cd ${MODEL_LANGUAGE} && importers.sh && cd ..

generate_alphabet.sh

build_lm.sh

train.sh

evaluate_lm.sh

package.sh
