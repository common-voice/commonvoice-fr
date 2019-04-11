CommonVoice -- DeepSpeech
=========================

L'objectif de ce repository est de réunir en un endroit les différentes tâches à effectuer afin d'arriver à la production d'un modèle [DeepSpeech] en français.
DeepSpeech est développé par la communauté avec le support de [Mozilla], vos données ne sont pas exploitées par des sociétés commerciales et votre vie privée est préservée.

DeepSpeech est un outil qui va transformer votre voix en texte. Avant d'arriver à ce résultat, il faut collecter des données afin d'entraîner cet outil à comprendre votre voix.

Pour ce faire, différents outils ont été mis en place par [Mozilla]. Le premier est [Common Voice], il est très important, c'est lui qui permet de récolter les voix. Sans ces données, impossible de faire fonctionner [DeepSpeech].
Sur ce site, vous pouvez soit offrir votre voix, soit valider les textes.

Un second outil est un collecteur de phrases [Sentence Collector]. En effet pour que vous puissiez donner votre voix dans [Common Voice], il faut des phrases et ces phrases doivent être libre de droits.

[CorporaCreator] est un outil en ligne de commande qui permet de nettoyer les phrases collectées par [Common Voice] et de produire un jeu de données mis à disposition par Common Voice. 


## Sentence Collector

Dans ce dépôt, nous loggons les taches spécifiques à la langue française qu'il faut effectuées sur le site [Sentence Collector] afin de simplifié au maximum la validation des phrases proposées.
Les [abréviations] par exemple ne sont pas connues de tous et dans [Common Voice] à la lecture cela peut poser problème.



## Common Voice

Dans ce dépôt, nous extrayons les phrases de différentes sources qui offrent leurs données en domaine public.
Par Exemple les données de l'Assemblée Nationale, du projet Gutenberg, etc.
Mais tout n'est pas encore extrait et un peu d'aide est la bienvenue pour par exemple. Voir le dossier [CommonVoice-Data] pour plus d'information. Les extracteurs sont écrits en [Python] et script Shell.

Si vous connaissez d'autres sources offrant des données dans le domaine public n'hésitez pas à ouvrir une [issue] afin que l'on puisse vérifier que les données peuvent être utilisées par le projet et éventuellement vous aidez dans l'extraction des données.


## CorporaCreator

Dans ce dépôt nous collectons les problèmes liés à la langue française afin d'améliorer la reconnaissance vocale. Par exemple, les [nombres] qui peuvent être assemblé différemment.


## DeepSpeech

L'objectif final de ce dépôt est évidemment un modèle DeepSpeech français qui puissent être utilisé par exemple dans un [assistant vocal] ou pour aider les personnes avec des déficiences visuelles ou motrices .
Une [image Docker] est actuellement en développement afin de facilité l'entraînement de [DeepSpeech].
Centralisation d'outil de construction et de nettoyage de jeux de données pour
CommonVoice et de production de modèles DeepSpeech en français.


## Conclusions

N'hésitez pas à participer selon vos capacités:

### Non technique:

- Proposer des phrases dans [Sentence Collector].
- Donner votre voix ou valider des voix sur [Common Voice].
- Partager les liens vers [Sentence Collector] et [Common Voice] sur les réseaux sociaux afin de faire connaître le projet et l'améliorer. 


### Technique:

- Améliorer la documentation via une [Pull Request].
- En venant discuter de comment aider sur Telegram en rejoignant le groupe [Common Voice fr].
- En répondant à une issue que vous souhaitez aider.
- En créant une [Pull Request] afin d'améliorer du code.

  [DeepSpeech]: <https://github.com/mozilla/DeepSpeech>
  [Mozilla]: <https://www.mozilla.org/fr/>
  [Common Voice]: <https://voice.mozilla.org/fr>
  [Sentence Collector]: <https://common-voice.github.io/sentence-collector/#/>
  [CorporaCreator]: <https://github.com/mozilla/CorporaCreator>
  [abréviations]: <https://github.com/Common-Voice/commonvoice-fr/issues/21>
  [CommonVoice-Data]: <https://github.com/Common-Voice/commonvoice-fr/tree/master/CommonVoice-Data>
  [Python]: <https://docs.python.org/fr/3/>
  [issue]: <https://github.com/Common-Voice/commonvoice-fr/issues/new>
  [nombres]: <https://github.com/mozilla/CorporaCreator/pull/87>
  [assistant vocal]: <https://fr.wikipedia.org/wiki/Assistant_personnel_intelligent>
  [image Docker]: <https://github.com/Common-Voice/commonvoice-fr/issues/24>
  [Pull Request]: <https://help.github.com/en/articles/about-pull-requests>
  [Common Voice fr]: <https://t.me/joinchat/A7h94U7VCFrCnXrDMff2Vw>
