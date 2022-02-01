#!/bin/sh

set -xe

THIS=$(dirname "$0")
<<<<<<< HEAD
export PATH=${THIS}:${THIS}/${MODEL_LANGUAGE}:$PATH
=======
export PATH="${THIS}:${THIS}/${MODEL_LANGUAGE}:${STT_DIR}/training/coqui_stt_training:$PATH"
>>>>>>> coqui-stt-1.0.0

export TF_CUDNN_RESET_RND_GEN_STATE=1

env

checks.sh

export TMP=/mnt/tmp
export TEMP=/mnt/tmp

. params.sh
<<<<<<< HEAD
. ${MODEL_LANGUAGE}/params.sh

if [ -x "${MODEL_LANGUAGE}/metadata.sh" ]; then
	. ${MODEL_LANGUAGE}/metadata.sh
=======
. ${HOMEDIR}/${MODEL_LANGUAGE}/params.sh

if [ -x "${HOMEDIR}/${MODEL_LANGUAGE}/metadata.sh" ]; then
	. ${HOMEDIR}/${MODEL_LANGUAGE}/metadata.sh
>>>>>>> coqui-stt-1.0.0
else
	echo "Please prepare metadata informations."
	exit 1
fi;

<<<<<<< HEAD
cd ${MODEL_LANGUAGE} && importers.sh && cd ..
=======
cd ${HOMEDIR}/${MODEL_LANGUAGE} && importers.sh && cd ${HOMEDIR}
>>>>>>> coqui-stt-1.0.0

generate_alphabet.sh

build_lm.sh

train.sh

evaluate_lm.sh

package.sh
