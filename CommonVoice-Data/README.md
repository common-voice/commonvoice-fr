Ce dossier contient les extracteurs et les données extraites de différentes sources:

## requirements
python>=3.6

## Data

Contient les données extraites des site web

## Tests

Ce dossier contient des fichiers avec des données test pour vérifier que les donnés sont extraites correctement.

## Adresses

Extracteurs d'adresses française.
Address data are extracted from [source: BANO](https://www.data.gouv.fr/fr/datasets/base-d-adresses-nationale-ouverte-bano/)

Fichier(s): bano.py

Licence: ODbL 

Usage: `$ python bano.py data/addresses`

see `$ python bano.py --help` for more info/options

## Débats Assemblée Nationale

Extacteurs des compte-rendus de séances de l'Assemblée Nationale Française [source: Assemblée Nationale] (http://data.assemblee-nationale.fr/travaux-parlementaires/debats)

License:  [Licence Ouverte / Open Licence] (http://data.assemblee-nationale.fr/licence-ouverte-open-licence)

Fichier(s) : debats-assemblee-nationale.sh, syceron.py

Le fichier debats-assemblee-nationale.sh vérifie que vous avez bien télécharger le ficher Syceronbrut.xml.zip, que vous l'avez extrait dans le réprtoire où vous executez ce fichier et qu'il n'y a plus de fichier .txt dans le répertoire data/debats-assemblee-nationale/, avant de lancer automatiquement l'extraction à l'aide du fichier syceron.py.

Usage: sh debats-assemblee-nationale.sh
(note that to launch this command you will need a shell to be able to execute this)



## Names
Names data are extracted from [source: INSEE](https://www.insee.fr)

Licence: NO LICENSE

> Ils [Les fichiers détail] peuvent être téléchargés gratuitement et les données contenues dans ces fichiers peuvent être réutilisées, y compris à des fins commerciales, sans licence et sans versement de redevance, dans le cadre des mentions légales sur le site.

see https://www.insee.fr/fr/information/1300614 for more info 

Usage: `$ python names.py data/names.txt`

see `$ python names.py --help` for more info/options

## Testing
`$ PYTHONPATH=. pytest tests`
