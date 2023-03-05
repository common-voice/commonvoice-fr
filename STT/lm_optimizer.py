#!/usr/bin/env python3
"""
Custom implementation of STT/lm_optimizer.py to catch the results of lm optimization and save to disk as yaml.
"""

from __future__ import absolute_import, print_function

import sys, os, yaml

def save_best_val(dict_to_save_as_yaml, path_to_yaml):
    if not os.path.exists(path_to_yaml):
        with open(path_to_yaml, "w") as f:
            yaml.dump(dict_to_save_as_yaml, f)


if __name__ == "__main__":
    try:
        from coqui_stt_training.train import early_training_checks
        from coqui_stt_training.util.config import (
            Config,
            initialize_globals_from_cli,
            log_error,
        )
        from coqui_stt_training.util import lm_optimize
    except ImportError:
        print("Training package is not installed. See training documentation.")
        raise
    
    initialize_globals_from_cli()
    early_training_checks()
    
    if not Config.scorer_path:
        log_error(
            "Missing --scorer_path: can't optimize scorer alpha and beta "
            "parameters without a scorer!"
        )
        sys.exit(1)

    if not Config.test_files:
        log_error(
            "You need to specify what files to use for evaluation via "
            "the --test_files flag."
        )
        sys.exit(1)

    results = lm_optimize.compute_lm_optimization()
    print(
        "Best params: lm_alpha={} and lm_beta={} with WER={}".format(
            results.get("lm_alpha"),
            results.get("lm_beta"),
            results.get("wer"),
        )
    )

    save_best_val(results, "/mnt/lm/opt_lm.yml")