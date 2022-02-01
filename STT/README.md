# Groupe de travail pour DeepSpeech en français

## Table des matières

- [Introduction](#introduction)
- [Canaux](#canaux)
- [Participer à DeepSpeech](#Participer-à-DeepSpeech)
- [Processus pour DeepSpeech fr](#Processus-pour-deepSpeech-fr)
- [Bien démarrer](#bien-démarrer)
  - [Installation et configuration](#Installation-et-configuration)
  - [Où trouver des jeux de données](#Ou-trouver-des-jeux-de-données)
  - [Speech-to-Text et Text-to-Speech](#Speech-to-Text-et-Text-to-Speech)
  - [La parole vers le texte et le texte vers la parole](#La-parole-vers-le-texte-et-le-texte-vers-la-parole)
- [Exemples](#exemples)
  - [Convertir la parole vers le texte](#Convertir-la-parole-vers-le-texte)
  - [Utiliser DeepSpeech pour vos projets webs](#Utiliser-DeepSpeech-pour-vos-projets-web)
- [Projets disponibles](#projets-disponibles)


Vous trouverez dans ce document l'ensemble des instructions, documentations... pour le projet Common Voice.

# Introduction

Le projet DeepSpeech est un autre projet de la fondation Mozilla, pour transformer les ondes sonores en texte à partir de l'algorithme d'apprentissage proposé par [Common Voice](https://github.com/Common-Voice/commonvoice-fr/tree/master/CommonVoice).

# Canaux

- **DeepSpeech** utilise le canal **Common Voice fr** sur [Matrix](https://github.com/mozfr/besogne/wiki/Matrix) pour la discussion et la coordination : [s’inscrire au groupe](https://chat.mozilla.org/#/room/#common-voice-fr:mozilla.org) 
- [Discourse Mozilla Francophone](https://discourse.mozilla.org/c/voice/fr)
- [Discourse Mozilla (anglais)](https://discourse.mozilla.org/c/voice)

# Participer à DeepSpeech _pour tous_

Le projet **DeepSpeech** utilise des jeux de données du projet **Common Voice fr**, vous pouvez aider à faire grandir cette base de données : [Participer à Common Voice](https://github.com/Common-Voice/commonvoice-fr/tree/master/CommonVoice#Participer-à-Common-Voice).

# Processus pour DeepSpeech fr

C'est un processus en deux grosses étapes :

1. Vous aidez à convertir du texte vers l'audio et l'audio en texte

## Bien démarrer

### Installation et configuration

- Les détails d'installation et de configuration sont disponible à la page de [Contribution](https://github.com/Common-Voice/commonvoice-fr/blob/master/DeepSpeech/CONTRIBUTING.md)

### Où trouver des jeux de données

- <https://commonvoice.mozilla.org/fr/datasets>

### Speech-to-Text et Text-to-Speech

- [Modèles DeepSpeech](https://github.com/mozilla/deepspeech)

### La parole vers le texte et le texte vers la parole (en fr)

- Common Voice Corpora Creator : [FR](https://github.com/Common-Voice/commonvoice-fr/voice-corpus-tool) [EN](https://github.com/mozilla/voice-corpus-tool)
- Common Voice Sentence Collector : [FR](https://github.com/Common-Voice/commonvoice-fr/sentence-collector) [EN](https://github.com/Common-Voice/sentence-collector)

## Exemples

### Convertir la parole vers le texte

- [convertir la parole en texte](https://hacks.mozilla.org/2018/09/speech-recognition-deepspeech/)

### Utiliser DeepSpeech pour vos projets web

- [C#](https://github.com/mozilla/DeepSpeech/tree/master/examples/net_framework)
- [NodeJS](https://github.com/mozilla/DeepSpeech/tree/master/examples/nodejs_wav)
- [Streaming NodeJS](https://github.com/mozilla/DeepSpeech/tree/master/examples/ffmpeg_vad_streaming)
- [transcription (streaming) Python](https://github.com/mozilla/DeepSpeech/tree/master/examples/vad_transcriber)

# Projets disponibles

- [mycroft](https://mycroft.ai/blog/deepspeech-update/) – assistant vocal open source
- [Leon](https://getleon.ai/) – assistant personnel open source
- [Baidu](https://github.com/mozilla/deepspeech) – implémentation d'une architecture DeepSpeech
- [Snips](https://snips.ai/) – assistant vocal décentralisé et privé
- FusionPBX – système de commutation téléphonique installé dans une organisation privée et servant à transcrire des messages téléphoniques
