#!/bin/bash

set -xe

pushd $STT_DIR
    if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
        IMPORT_AS_ENGLISH="--normalize"
    fi;

    if [ "${LM_ADD_EXCLUDED_MAX_SEC}" = "1" ]; then
        SAVE_EXCLUDED_MAX_SEC="--save_excluded_max_sec_to_disk /mnt/extracted/data/MLS/MLS_excluded_lm.txt"
    fi;

    if [ ! -f "/mnt/extracted/data/MLS/MLS_train.csv" ]; then
        python ${STT_DIR}/bin/import_mls.py \
            ${IMPORT_AS_ENGLISH} \
            ${IMPORTERS_VALIDATE_LOCALE} \
            ${SAVE_EXCLUDED_MAX_SEC} \
            -l french \
            /mnt/extracted/data/MLS/
    fi;

    if [ "${LM_ADD_EXCLUDED_MAX_SEC}" = "1" ]; then
        mv /mnt/extracted/data/MLS/MLS_excluded_lm.txt /mnt/extracted/_mls_lm.txt
    fi;
popd