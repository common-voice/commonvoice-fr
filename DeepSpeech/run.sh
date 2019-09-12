#!/bin/sh

set -xe

export PATH=$(dirname "$0"):$PATH

env

checks.sh

export TMP=/mnt/tmp
export TEMP=/mnt/tmp

source run_${MODEL_LANGUAGE}.sh

package.sh
