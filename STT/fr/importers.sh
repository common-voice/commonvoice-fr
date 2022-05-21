#!/bin/sh

set -xe

# If the environment contains urls to downlaod a CV personal archive of the user
# and there is a checkpoint mounted but no output_graph,
# it's likely we want to downlaod our custom archive as data
# and start fine-tuning from our checkpoint.
if [ \
    -f "/transfer-checkpoint/checkpoint" -a \
    ! -f "/mnt/models/output_graph.tflite" -a \
    -z "${CV_PERSONAL_FIRST_URL}" -a \
    -z "${CV_PERSONAL_SECOND_URL}" \
]; then
    ../import_cv_perso.sh
else
    ../import_cv.sh

    ../import_lingualibre.sh

    import_trainingspeech.sh

    import_slr57.sh

    ../import_m-ailabs.sh

    ./import_atthack.sh

    ./import_mls.sh

    #./import_ccpmf.sh
fi;