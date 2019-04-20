# Groupe de travail pour Common Voice en français

## Table of contents

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

Vous trouverez dans ce document l'ensemble des instructions, documentations... pour le projet Common Voice.

# Introduction

Le projet Common Voice est une initiative de Mozilla pour aider à apprendre aux machines à parler comme tout un chacun. Il va permettre de collecter les données pour fournir du contenu aux algorithmes comme pour [DeepSpeech](https://github.com/Common-Voice/commonvoice-fr/wiki/DeepSpeech)

# Canaux

- **Common Voice fr** sur Telegram pour la discussion/coordination : [s'inscrire au groupe](https://t.me/joinchat/A7h94U7VCFrCnXrDMff2Vw)
- [Discourse Mozilla](https://discourse.mozilla.org/c/voice)

# Participer à Common Voice

## La voix

Il est possible de parler et d'écouter des voix pour faire grossir la base de données.

- [site officiel Common Voice](https://voice.mozilla.org)
- [Parler](https://voice.mozilla.org/fr/speak)
- [Ecouter](https://voice.mozilla.org/fr/listen)

### Proposer et valider de nouvelles phrases

Plusieurs étapes :

1. Vous devez posséder un compte sur [Common Voice](https://voice.mozilla.org)
2. Identifiez-vous sur le [Collecteur de phrases](https://common-voice.github.io/sentence-collector/#/login) avec les identifiants de Common voice
3. Pour valider les phrases, il faut utiliser la [page de validation](https://common-voice.github.io/sentence-collector/#/review/fr)
4. Si vous souhaitez ajouter de nouvelles phrases, vous devez vous rendre sur [Ajouter une nouvelle phrase](https://common-voice.github.io/sentence-collector/#/add)

## Processus pour Common Voice fr

C'est un processus en deux grosses étapes :

1. Construction d'un corpus de texte à faire lire (voir les contraintes ci-dessous).

2. Contribution vocale :

  - Différents genres
  - Différents âges
  - Différents accents

3. Une fois collectées suffisamment de variétés et de quantité (des centaines d'heures d'audio), il faut construire des ensembles pour l'apprentissage du modèle français.

### Étape en cours

On essaie de construire un premier ensemble de départ – ~10k phrases de sources variées – pour lancer une langue. Ensuite prend place le processus **manuel** de validation des envois pour vérifier un minimum de qualité. Pour faire partie de cette équipe de validateurs, prenez langue sur <https://discourse.mozilla.org/c/voice>.

### Construction du corpus de texte

#### Contraintes

- Common Voice redistribue en [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.fr "Creative Commons – CC0 1.0 universel"). Il faut donc des corpus de texte **compatibles**.
- Texte représentatif (dialogues de film, débats, théâtre)
- Différents registres de langue nécessaires
- Normalisation des nombres (chiffres romains aussi)
- **Voir `commonvoice-fr` pour du code qui normalise proprement le texte**

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
  - ~2.2M phrases, 42M mots, 430k mots uniques

- <http://www.cuisine-libre.fr/>

  - Licence domaine public
  - HTML, texte brut (UTF-8)
  - À PARSER

- <http://libretheatre.fr/>

  - Licence domaine public
  - HTML, texte brut (UTF-8)
  - Parser en cours : <https://github.com/Common-Voice/commonvoice-fr>

- <http://www.inlibroveritas.net/>

  - [Licence Art Libre – LAL 1.3](http://artlibre.org/licence/lal)
  - **PDF À PARSER**

### Liens à garder pour plus tard

- Corpus vocaux scientifiques en français sur [Ortolang](https://www.ortolang.fr/market/corpora?filters=%7B%22corporaType.id%22:%5B%22speech_corpora%22%5D%7D&viewMode=tile&orderProp=rank&orderDir=desc)
- <http://golem13.fr/5000-films-tombes-dans-le-domaine-public-a-telecharger-gratuitement/\>
- <https://www.apar.tv/cinema/700-films-rares-et-gratuits-disponibles-ici-et-maintenant/\>

### Rajouter des phrases

<https://common-voice.github.io/sentence-collector/#/add\>

# Annonces et articles intéressants

## Section Presse annonce Mozilla

- [Common Voice devient multilingue et s'enrichit de nouvelles langues](https://blog.mozilla.org/press-fr/2018/06/07/common-voice-devient-multilingue-et-senrichit-de-nouvelles-langues/) – 7 juin 2018
- [Common Voice : Mutualiser nos voix – Mozilla publie le plus grand jeu de données vocales transcrites du domaine public à ce jour](https://blog.mozilla.org/press-fr/2019/02/28/common-voice-mutualiser-nos-voix-mozilla-publie-le-plus-grand-jeu-de-donnees-vocales-transcrites-du-domaine-public-a-ce-jour/) – 28 février 2019

## Article de la communauté francophone

- [Haussons la voix tous ensemble pour le Web](https://blog.mozfr.org/post/2017/07/Haussons-la-voix-tous-ensemble-pour-le-Web-Common-Voice) – Traduction de l'article de Daniel Kessler du 19 juillet 2017 par la communauté Mozilla francophone
- [Mozilla ouvre la voix](https://blog.mozfr.org/post/2017/07/Mozilla-ouvre-la-voix-reconnaissance-vocale) – Article de Kelly Davis du 28 juillet 2017 sur les plans de Mozilla d'ouvrir la reconnaissance vocale traduit par la communauté Mozilla francophone

## Interview

- [Common Voice arrive en France !](https://www.ausy.fr/fr/actualites-techniques/common-voice-arrive-en-france) : Christophe Villeneuve, Rep et TechSpeakers pour Mozilla, le 28 oct. 2018
- [Common voice : Mozilla reconnaissance vocale](https://www.blogdumoderateur.com/common-voice-mozilla-reconnaissance-vocale/) : Kelly Davis, chercheur en machine learning chez Mozilla, le 29 nov. 2018
- [VIDÉO. Aidez Mozilla à créer la reconnaissance vocale en breton !](https://laseyne.maville.com/actu/actudet_-video.-aidez-mozilla-a-creer-la-reconnaissance-vocale-en-breton-_54135-3590536_actu.Htm "VIDÉO. Aidez Mozilla à créer la reconnaissance vocale en breton ! - La Seyne.maville.com") : Alexandre Lissy, ingénieur de recherche chez Mozilla, le 30 nov. 2018

## Autres articles

- [La guerre des assistants vocaux commence aujourd'hui en France](https://www.forbes.fr/technologie/la-guerre-des-assistants-vocaux-commence-aujourdhui-en-france/)
- [Mozilla veut amplifier son virage sur les contenus personnalisés](https://www.lesechos.fr/07/03/2018/lesechos.fr/0301387403003_mozilla-veut-amplifier-son-virage-sur-les-contenus-personnalises.htm)
- [common voice pour que la voix soit libre](https://framablog.org/2018/12/19/projet-common-voice-pour-que-la-voix-soit-libre/) – Framablog du 19 décembre 2018
