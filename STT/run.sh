#!/bin/sh

set -xe

THIS=$(dirname "$0")
export PATH="${THIS}:${THIS}/${MODEL_LANGUAGE}:${STT_DIR}/training/coqui_stt_training:$PATH"

export TF_CUDNN_RESET_RND_GEN_STATE=1

env

checks.sh

export TMP=/mnt/tmp
export TEMP=/mnt/tmp

. params.sh
. ${HOMEDIR}/${MODEL_LANGUAGE}/params.sh

if [ -x "${HOMEDIR}/${MODEL_LANGUAGE}/metadata.sh" ]; then
	. ${HOMEDIR}/${MODEL_LANGUAGE}/metadata.sh
else
	echo "Please prepare metadata informations."
	exit 1
fi;

cd ${HOMEDIR}/${MODEL_LANGUAGE} && importers.sh && cd ${HOMEDIR}

generate_alphabet.sh

build_lm.sh

train.sh

evaluate_lm.sh

package.sh
