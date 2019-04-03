Ce dossier contient les extracteurs et les données extraites de différentes sources:

## requirements
python>=3.6
Voir aussi le fichier requirements.txt

## Data

Contiens les données extraites des sites web

## Tests

Ce dossier contient des fichiers avec des données tests pour vérifier que les données sont extraites correctement.

## Adresses

Extracteurs d'adresses françaises.
Address data are extracted from [source: BANO](https://www.data.gouv.fr/fr/datasets/base-d-adresses-nationale-ouverte-bano/)

Licence: ODbL 

Fichier(s): bano.py

Usage: `$ python bano.py data/addresses`

see `$ python bano.py --help` for more info/options

## Débats Assemblée Nationale

Extracteurs des comptes-rendus de séances de l'Assemblée Nationale Française [source: Assemblée Nationale] (http://data.assemblee-nationale.fr/travaux-parlementaires/debats)

Licence:  [Licence Ouverte / Open Licence] (http://data.assemblee-nationale.fr/licence-ouverte-open-licence)

Fichier(s) : debats-assemblee-nationale.sh, syceron.py

Le fichier debats-assemblee-nationale.sh vérifie que vous avez bien télécharger le ficher Syceronbrut.xml.zip, que vous l'avez extrait dans le répertoire où vous exécutez ce fichier et qu'il n'y a plus de fichier .txt dans le répertoire data/debats-assemblee-nationale/, avant de lancer automatiquement l'extraction à l'aide du fichier syceron.py.

Usage: `sh debats-assemblee-nationale.sh`
(Afin de lancer cette commande vous devez disposer d'un shell.)


## Length.py

Pas utilisé, probablement à nettoyer


## Libre Théatre

Extracteurs des pièces de théâtre.
Le site Libre Théâtre met à disposition une bibliothèque numérique d’œuvres théâtrales.
Une collection du domaine public en téléchargement gratuit :  les pièces de théâtre les plus célèbres du répertoire français, mais aussi des oeuvres originales moins connues, mais remarquables par leur empreinte dans l’histoire du théâtre, par les thématiques évoquées, leur esthétique ou leur dramaturgie.  Vous pouvez rechercher des pièces en parcourant le site Libre Théâtre à partir de l’histoire du théâtre, à partir de la description de l’oeuvre théâtrale d’un auteur ou grâce à des critères de recherche précis (auteur, titre, distribution, genre, époque…) via la base de données data.libreatre.fr. [source: https://libretheatre.fr/](https://libretheatre.fr)

Licence: [domaine public](https://fr.wikipedia.org/wiki/Domaine_public_(propri%C3%A9t%C3%A9_intellectuelle))

Fichier(s) : libretheatre.py

Usage: `$ python libretheatre.py data/libretheatre`

see `$ python libretheatre.py --help` for more info/options


## Projet Gutenberg

Le Projet Gutenberg offre plus de 54.000 livres électroniques en accès libre. Vous trouverez ici la grande littérature mondiale, particulièrement les ouvrages anciens désormais libres de droits. [source: Projet Gutenberg](http://www.gutenberg.org/wiki/FR_Page_d%27Accueil)
L'extracteur télécharge les livres en français qui sont dans le domaine public puis les parses en phrases prêtes pour Common Voice.

Licence: [domaine public](https://fr.wikipedia.org/wiki/Domaine_public_(propri%C3%A9t%C3%A9_intellectuelle))

Fichier(s) : livres-projet-gutenberg.sh, project-gutenberg.py

Le fichier livres-projet-gutenberg.sh vérifie que vous n'avez pas de fichier txt dans le répertoire data/gutenberg. S'il y a des fichiers alors il lancera le script project-gutenberg.py en considérant que le nom du fichier est l'identifiant d'un livre et l'extraira. S'il n'y a pas de fichiers txt dans le répertoire data/gutenberg alors il lancera le fichier project-gutenberg.py et extraira 1000 livres au hasard.

Usage: `sh livres-projet-gutenberg.sh`
(Afin de lancer cette commande vous devez disposer d'un shell.)
Vous pouvez également lancer le script python directement. Pour plus d'infos et voir les options: `$ python project-gutenberg.py --help`


## Names

Names data are extracted from [source: INSEE](https://www.insee.fr)

Licence: NO LICENSE

> Ils [Les fichiers détail] peuvent être téléchargés gratuitement et les données contenues dans ces fichiers peuvent être réutilisées, y compris à des fins commerciales, sans licence et sans versement de redevance, dans le cadre des mentions légales sur le site.

see https://www.insee.fr/fr/information/1300614 for more info 

Usage: `$ python names.py data/names.txt`

see `$ python names.py --help` for more info/options


## Utils.py

Ce fichier contient des méthodes utiles qui sont appelées dans les autres scripts d'extraction.


## Testing

Pour tester vous pouvez lancer la commande suivante:
`$ PYTHONPATH=. pytest tests`
Cela exécutera les scripts de tests qui sont dans le répertoire tests.

