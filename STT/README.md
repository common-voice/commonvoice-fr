# Groupe de travail pour la reconaissance vocal du français (CommonVoice-fr)

## Table des matières

- [Introduction](#introduction)
- [Canaux](#canaux)
- [Participer à CommonVoice-fr](#Participer-à-STT)
- [Processus pour CommonVoice-fr](#Processus-pour-CommonVoice-fr)
- [Bien démarrer](#bien-démarrer)
  - [Installation et configuration](#Installation-et-configuration)
  - [Où trouver des jeux de données](#Ou-trouver-des-jeux-de-données)
  - [Speech-to-Text et Text-to-Speech](#Speech-to-Text-et-Text-to-Speech)
  - [La parole vers le texte et le texte vers la parole](#La-parole-vers-le-texte-et-le-texte-vers-la-parole)
- [Exemples](#exemples)
  - [Convertir la parole vers le texte](#Convertir-la-parole-vers-le-texte)
  - [Utiliser STT pour vos projets webs](#Utiliser-STT-pour-vos-projets-web)
- [Projets disponibles](#projets-disponibles)


Vous trouverez dans ce document l'ensemble des instructions, documentations... pour le projet Common Voice.

# Introduction

> STT: Speech-To-Text

> Ou l'art de transcrire la voix en texte.

Le projet CommonVoice FR utilise 🐸-STT ([Coqui-STT](https://github.com/coqui-ai/STT)), l'implémentation suivante du projet [DeepSpeech](https://github.com/mozilla/DeepSpeech) de la fondation Mozilla, pour continuer à transformer les ondes sonores en texte à partir de l'algorithme d'apprentissage proposé par la communauté.

# Canaux

- **CommonVoice-fr** utilise le canal **Common Voice FR** sur [Matrix](https://github.com/mozfr/besogne/wiki/Matrix) pour la discussion et la coordination : [s’inscrire au groupe](https://chat.mozilla.org/#/room/#common-voice-fr:mozilla.org) 
- [Discourse Mozilla Francophone](https://discourse.mozilla.org/c/voice/fr)
- [Discourse Mozilla (anglais)](https://discourse.mozilla.org/c/voice)

# Participer à CommonVoice _pour tous_

Le projet **CommonVoice-fr** utilise des jeux de données du projet **Common Voice fr**, vous pouvez aider à faire grandir cette base de données : [Participer à Common Voice](https://github.com/Common-Voice/commonvoice-fr/tree/master/CommonVoice#Participer-à-Common-Voice).

# Processus pour CommonVoice-fr

C'est un processus en deux grosses étapes :

1. Vous aidez à convertir du texte vers l'audio et l'audio en texte

## Bien démarrer

### Installation et configuration

- Les détails d'installation et de configuration sont disponible à la page de [Contribution](https://github.com/Common-Voice/commonvoice-fr/blob/master/STT/CONTRIBUTING.md) (en anglais).

- Pour l'ajustement des modèles francophones sur vos données personnelles de CommonVoice, lisez [cet article sur les forums de Mozilla](https://discourse.mozilla.org/t/entrainer-des-modeles-sur-mesure-avec-commonvoice-fr/97503?u=skeilnet)

### Où trouver des jeux de données

- <https://commonvoice.mozilla.org/fr/datasets>

### Speech-to-Text et Text-to-Speech

- [Modèles STT](https://coqui.ai/models)

### La parole vers le texte et le texte vers la parole (en fr)

- Common Voice Corpora Creator : [FR](https://github.com/Common-Voice/commonvoice-fr/voice-corpus-tool) [EN](https://github.com/mozilla/voice-corpus-tool)
- Common Voice Sentence Collector : [FR](https://github.com/Common-Voice/commonvoice-fr/sentence-collector) [EN](https://github.com/Common-Voice/sentence-collector)

## Exemples

### Convertir la parole vers le texte

- [convertir la parole en texte](https://hacks.mozilla.org/2018/09/speech-recognition-deepspeech/)

### Utiliser STT pour vos projets web

- [C#](https://github.com/coqui-ai/STT/tree/master/examples/net_framework)
- [NodeJS](https://github.com/coqui-ai/STT/tree/master/examples/nodejs_wav)
- [Streaming NodeJS](https://github.com/coqui-ai/STT/tree/master/examples/ffmpeg_vad_streaming)
- [transcription (streaming) Python](https://github.com/coqui-ai/STT/tree/master/examples/vad_transcriber)

# Projets disponibles

- [mycroft](https://mycroft.ai/blog/STT-update/) – assistant vocal open source
- [Leon](https://getleon.ai/) – assistant personnel open source
- [Coqui-STT](https://github.com/coqui-ai/STT) – implémentation d'une architecture STT
- [Snips](https://snips.ai/) – assistant vocal décentralisé et privé
- FusionPBX – système de commutation téléphonique installé dans une organisation privée et servant à transcrire des messages téléphoniques
