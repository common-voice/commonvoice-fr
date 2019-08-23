# Groupe de travail pour Common Voice en français

## Table des matières

- [Introduction](#introduction)
- [Canaux](#canaux)
- [Participer à Common Voice](#Participer-à-Common-Voice)

  - [La voix](#la-voix)

  - [Proposer et valider de nouvelles phrases](#Proposer-et-valider-de-nouvelles-phrases)

- [Processus pour Common Voice fr](#Processus-pour-Common-Voice-fr)

  - [Étape en cours](#etape-en-cours)

  - [Construction du corpus de texte](#construction-du-corpus-de-texte)

- [Liens à garder pour plus tard](#Liens-à-garder-pour-plus-tard)

- [Rajouter des phrases](#Rajouter-des-phrases)

Vous trouverez dans ce document l’ensemble des instructions, documentations… pour le projet Common Voice.

# Introduction

Le projet Common Voice est une initiative de Mozilla pour aider à apprendre aux machines comment les humains parlent vraiment. Il va permettre de collecter des données pour fournir du contenu aux algorithmes comme [Deep Speech](https://github.com/Common-Voice/commonvoice-fr/wiki/DeepSpeech).

# Canaux

- **Common Voice fr** sur Telegram pour la discussion et la coordination : [s’inscrire au groupe](https://t.me/joinchat/A7h94U7VCFrCnXrDMff2Vw)
- [Discourse Mozilla Francophone](https://discourse.mozilla.org/c/voice/fr)
- [Discourse Mozilla (anglais)](https://discourse.mozilla.org/c/voice)

# Participer à Common Voice

## La voix

Il est possible de parler et d’écouter des voix pour faire grossir la base de données.

- [Site officiel Common Voice](https://voice.mozilla.org)
- [Parler](https://voice.mozilla.org/fr/speak)
- [Écouter](https://voice.mozilla.org/fr/listen)

### Proposer et valider de nouvelles phrases

Plusieurs étapes :

1. Vous devez posséder un compte sur [Common Voice](https://voice.mozilla.org).
2. Identifiez-vous sur le [Collecteur de phrases](https://common-voice.github.io/sentence-collector/#/login) avec vos identifiants de Common Voice.
3. Pour valider les phrases, il faut utiliser la [page de validation](https://common-voice.github.io/sentence-collector/#/review/fr).
4. Si vous souhaitez ajouter de nouvelles phrases, vous devez vous rendre sur [Ajouter une nouvelle phrase](https://common-voice.github.io/sentence-collector/#/add)

## Processus pour Common Voice fr

C’est un processus en deux grosses étapes :

1. Construction d’un corpus de texte à faire lire (voir les contraintes ci-dessous).

2. Contribution vocale :

  - différents genres
  - différents âges
  - différents accents

3. Une fois collectées suffisamment de variétés et de quantité (des centaines d'heures d'audio), il faut construire des ensembles pour l'apprentissage du modèle français.

### Étape en cours

Le corpus de texte est suffisant pour collecter de la données vocale. De nouvelles sources de texte sont toujours bienvenues, cependant. Pour en discuter <https://discourse.mozilla.org/c/voice/fr>.

### Construction du corpus de texte

#### Méthode

Pour construire initialement et continuer à améliorer le corpus de texte, le processus est :
 - Identification d'un jeu de données intéressant (licence, volume)
 - Écriture d'un outil d'importation avec les paramètres adéquats (filtrage, etc.)
 - Transformation de la source complète en texte brut UTF-8 importé dans `CommonVoice-data/`
 - Envoi sur Sentence Collector pour validation et inclusion : https://common-voice.github.io/sentence-collector/

#### Contraintes

- Common Voice redistribue en [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.fr "Creative Commons – CC0 1.0 universel"). Il faut donc des corpus de texte **compatibles**.
- Texte représentatif (dialogues de film, débats, théâtre).
- Différents registres de langue nécessaires.
- Normalisation des nombres (chiffres romains aussi).
- **Voir `commonvoice-fr` pour du code qui normalise proprement le texte**.

#### Sources de données en CC0

- <http://data.assemblee-nationale.fr/>

  - Licence ≃ CC0, avec attribution
  - Débats en XML
  - Parser qui commence à fonctionner : <https://github.com/Common-Voice/commonvoice-fr>
  - ~1.4M phrases, 35M mots, 110k mots uniques
  - ~40k mots importés sur Crowdin (20180511)

- <https://www.gutenberg.org/>

  - Licence domaine public
  - HTML, ePUB, Kindle et texte brut (UTF-8)
  - Parser qui commence à fonctionner : <https://github.com/Common-Voice/commonvoice-fr>
  - Premiers essais, 1 000 livres extraits au hasard sur la langue française
  - ~2,2M phrases, 42M mots, 430k mots uniques

- <http://www.cuisine-libre.fr/>

  - Licence domaine public
  - HTML, texte brut (UTF-8)
  - À PARSER

- <http://libretheatre.fr/>

  - Licence domaine public
  - HTML, texte brut (UTF-8)
  - Parser en cours <https://github.com/Common-Voice/commonvoice-fr>

- <https://framabook.org/>

  - Différentes licences, dont certains livres en CC0
  - epub, LaTeX, PDF
  - Parser en cours <https://github.com/Common-Voice/commonvoice-fr>

- <http://www.inlibroveritas.net/>

  - [Licence Art Libre – LAL 1.3](http://artlibre.org/licence/lal)
  - **PDF À PARSER**

Les sources des données sont disponibles à partir du projet [Common Voice Data](https://github.com/Common-Voice/commonvoice-fr/tree/master/CommonVoice-Data)

### Liens à garder pour plus tard

- Corpus vocaux scientifiques en français sur [Ortolang](https://www.ortolang.fr/market/corpora?filters=%7B%22corporaType.id%22:%5B%22speech_corpora%22%5D%7D&viewMode=tile&orderProp=rank&orderDir=desc)
- <http://golem13.fr/5000-films-tombes-dans-le-domaine-public-a-telecharger-gratuitement/>
- <https://www.apar.tv/cinema/700-films-rares-et-gratuits-disponibles-ici-et-maintenant/>

### Rajouter des phrases

<https://common-voice.github.io/sentence-collector/#/add>
