# Dockerfile for producing french model

## Prerequistes:

* Ensure you have a running setup of `NVIDIA Docker`
* Prepare a host directory with enough space for training / producing intermediate data (100GB ?).
* Ensure it's writable by `trainer` (uid 999) user (defined in the Dockerfile).
* For Common Voice dataset, please make sure you have downloaded the dataset prior to running (behind email)
  Place `fr.tar.gz` (sha1 value should be `30dbf694ddc3951829c894b91328f4cf10179dcf`) inside your host directory,
  in a `sources/` subdirectory.

## Build the image:

```
$ docker build -f Dockerfile.train.fr .
```

Several parameters can be customized:
 - `ds_repo` to fetch DeepSpeech from a different repo than upstream
 - `ds_branch` to checkout a specific branch / commit
 - `ds_sha1` commit to pull from when installing pre-built binaries
 - `kenlm_repo`, `kenlm_branch` for the same parameters for KenLM
 - `english_compatible` set to 1 if you want the importers to be run in
    "English-compatible mode": this will affect behavior such as english
    alphabet file can be re-used, when doing transfer-learning from English
    checkpoints for example.

Some parameters for the model itself:
 - `batch_size` to specify the batch size for training, dev and test dataset
 - `epoch` to specify the number of epochs to run training for
 - `learning_rate` to define the learning rate of the network
 - `dropout` to define the dropout applied
 - `lm_alpha`, `lm_beta` to control language model alpha and beta parameters

Default values should provide good experience.

The default batch size has been tested with this mix of dataset:
 - Common Voice French, released on 2019, february 14th
 - TrainingSpeech as of 2019, april 11th
 - Lingua Libre as of 2019, may 3rd

### Transfer learning from English

To perform transfer learning, please download and make a read-to-use directory
containing the checkpoint to use. Ready-to-use means directly re-usable checkpoints
files, with proper `checkpoint` descriptor as TensorFlow produces.

To use an existing checkpoint, just ensure the `docker run` includes a mount such as:
`type=bind,src=PATH/TO/CHECKPOINTS,dst=/transfer-checkpoint`. Upon running, data
will be copied from that place.

## Hardware

Training successfull on:
 - 64GB RAM
 - 2x RTX 2080 Ti
 - Debian Sid, kernel 4.19, driver 418.56
 - With ~250h of audio, one training epoch takes ~15min, and validation takes ~50s

## Run the image:

The `mount` option is really important: this is where intermediate files, training, checkpoints as
well as final model files will be produced.

```
$ docker run --runtime=nvidia --mount type=bind,src=PATH/TO/HOST/DIRECTORY,dst=/mnt <docker-image-id>
```

Training parameters can be changed at runtime as well using environment variables.
