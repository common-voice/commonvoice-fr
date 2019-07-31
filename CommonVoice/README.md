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

- [Annonces et articles intéressants](#Annonces-et-articles-intéressants)

  - [Section Presse annonce Mozilla](#Section-Presse-annonce-Mozilla)

  - [Article de la communauté francophone](#article-de-la-communauté-francophone)

  - [Interview](#interview)

  - [Autres articles](#autres-articles)

  - [Conférences](#conférences)

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

- <http://www.cuisine-libre.fr/>

  - Licence domaine public
  - HTML, texte brut (UTF-8)
  - À PARSER

- <http://libretheatre.fr/>

  - Licence domaine public
  - HTML, texte brut (UTF-8)
  - Parser en cours <https://github.com/Common-Voice/commonvoice-fr>



- <http://www.inlibroveritas.net/>

  - [Licence Art Libre – LAL 1.3](http://artlibre.org/licence/lal)
  - **PDF À PARSER**

### Liens à garder pour plus tard

- Corpus vocaux scientifiques en français sur [Ortolang](https://www.ortolang.fr/market/corpora?filters=%7B%22corporaType.id%22:%5B%22speech_corpora%22%5D%7D&viewMode=tile&orderProp=rank&orderDir=desc)
- <http://golem13.fr/5000-films-tombes-dans-le-domaine-public-a-telecharger-gratuitement/>
- <https://www.apar.tv/cinema/700-films-rares-et-gratuits-disponibles-ici-et-maintenant/>

### Rajouter des phrases

<https://common-voice.github.io/sentence-collector/#/add>

# Annonces et articles intéressants

## Section Presse annonce Mozilla

- [Common Voice devient multilingue et s’enrichit de nouvelles langues](https://blog.mozilla.org/press-fr/2018/06/07/common-voice-devient-multilingue-et-senrichit-de-nouvelles-langues/) – 7 juin 2018
- [Common Voice : Mutualiser nos voix – Mozilla publie le plus grand jeu de données vocales transcrites du domaine public à ce jour](https://blog.mozilla.org/press-fr/2019/02/28/common-voice-mutualiser-nos-voix-mozilla-publie-le-plus-grand-jeu-de-donnees-vocales-transcrites-du-domaine-public-a-ce-jour/) – 28 février 2019

## Article de la communauté francophone

- [Haussons la voix tous ensemble pour le Web](https://blog.mozfr.org/post/2017/07/Haussons-la-voix-tous-ensemble-pour-le-Web-Common-Voice) – traduction de l’article de Daniel Kessler du 19 juillet 2017 par la communauté Mozilla francophone
- [Mozilla ouvre la voix](https://blog.mozfr.org/post/2017/07/Mozilla-ouvre-la-voix-reconnaissance-vocale) – article de Kelly Davis du 28 juillet 2017 sur les plans de Mozilla d’ouvrir la reconnaissance vocale traduit par la communauté Mozilla francophone

## Interview

- [Common Voice arrive en France !](https://www.ausy.fr/fr/actualites-techniques/common-voice-arrive-en-france) : Christophe Villeneuve, Rep et TechSpeakers pour Mozilla, le 28 oct. 2018
- [Common Voice et Deep Speech : les projets de Mozilla pour développer des solutions de reconnaissance vocale](https://www.blogdumoderateur.com/common-voice-mozilla-reconnaissance-vocale/) : Kelly Davis, chercheur en machine learning chez Mozilla, le 29 nov. 2018
- [VIDÉO. Aidez Mozilla à créer la reconnaissance vocale en breton !](https://laseyne.maville.com/actu/actudet_-video.-aidez-mozilla-a-creer-la-reconnaissance-vocale-en-breton-_54135-3590536_actu.Htm "VIDÉO. Aidez Mozilla à créer la reconnaissance vocale en breton ! – La Seyne.maville.com") : Alexandre Lissy, ingénieur de recherche chez Mozilla, le 30 nov. 2018

## Autres articles

- [La guerre des assistants vocaux commence aujourd’hui en France](https://www.forbes.fr/technologie/la-guerre-des-assistants-vocaux-commence-aujourdhui-en-france/) : Audrey Chabal, le 12 juin 2018, avec propos de Sylvestre Ledru de Mozilla
- [Projet Common Voice : pour que la voix soit libre](https://framablog.org/2018/12/19/projet-common-voice-pour-que-la-voix-soit-libre/) – Framasoft sur le Framablog du 19 déc. 2018
- [Faire de la reconnaissance vocale un bien commun](https://www.humanite.fr/faire-de-la-reconnaissance-vocale-un-bien-commun-675371/) – L'Humanité du 31 Juil. 2019

## Conférences

- [Common Voice](https://www.slideshare.net/hellosct1/common-voice) – L'Humanité du 9 juin 2019
- [Voix et machines](https://www.slideshare.net/hellosct1/voix-et-machines) – L'Humanité du 7 Juil. 2019
