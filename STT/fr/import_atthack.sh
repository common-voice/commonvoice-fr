#!/bin/bash

set -xe

pushd $STT_DIR
    if [ "${ENGLISH_COMPATIBLE}" = "1" ]; then
        IMPORT_AS_ENGLISH="--normalize"
    fi;

    if [ ! -f "/mnt/extracted/data/Att-HACK/Att-HACK_train.csv" ]; then
        if [ "${LM_ADD_EXCLUDED_MAX_SEC}" = "1" ]; then
            SAVE_EXCLUDED_MAX_SEC="--save_excluded_max_sec_to_disk /mnt/extracted/data/Att-HACK/Att-HACK_excluded_lm.txt"
        fi;

        python ${STT_DIR}/bin/import_atthack.py \
            ${IMPORT_AS_ENGLISH} \
            ${IMPORTERS_VALIDATE_LOCALE} \
            ${SAVE_EXCLUDED_MAX_SEC} \
            /mnt/extracted/data/Att-HACK/

        if [ "${LM_ADD_EXCLUDED_MAX_SEC}" = "1" ]; then
            mv /mnt/extracted/data/Att-HACK/Att-HACK_excluded_lm.txt /mnt/extracted/_att-hack_lm.txt
        fi;
    fi;
popd