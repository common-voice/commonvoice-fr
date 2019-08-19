#!/bin/bash

set -xe

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

# Checking with basic LDC93S1 before running into heavy-load
pushd $HOME/ds/
	./bin/run-tc-ldc93s1_new.sh 2
popd
