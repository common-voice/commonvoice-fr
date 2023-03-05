#!/bin/bash

set -xe

sudo id

# Workaround libnvidia-ml.so: https://github.com/NVIDIA/nvidia-docker/issues/854#issuecomment-451464721
sudo /sbin/ldconfig

nvidia-smi

for dir in $(find /mnt/ -maxdepth 1 -type d);
do
    echo "Checking ${dir} ..."
    if [ ! -w "${dir}" ]; then
        echo "Directory ${dir} is not writeable, sorry."
	exit 1
    fi;
done;

for subdir in sources extracted checkpoints models lm tmp;
do
    if [ ! -d "/mnt/${subdir}" ]; then
        mkdir /mnt/${subdir}
    fi;
done;

mkdir /mnt/extracted/data/ || true

python -c "import tensorflow as tf; tf.test.is_gpu_available()"

# Checking with basic LDC93S1 before running into heavy-load
pushd ${STT_DIR}
	./bin/run-ci-ldc93s1_new.sh 2 16000
popd
