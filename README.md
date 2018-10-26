## requirements
python>=3.6

## Addresses

Address data are extracted from [source: BANO](https://www.data.gouv.fr/fr/datasets/base-d-adresses-nationale-ouverte-bano/)

Licence: ODbL 

Usage: `$ python bano.py data/addresses`

see `$ python bano.py --help` for more info/options

## Names
Names data are extracted from [source: INSEE](https://www.insee.fr)

Licence: NO LICENSE

> Ils [Les fichiers détail] peuvent être téléchargés gratuitement et les données contenues dans ces fichiers peuvent être réutilisées, y compris à des fins commerciales, sans licence et sans versement de redevance, dans le cadre des mentions légales sur le site.

see https://www.insee.fr/fr/information/1300614 for more info 

Usage: `$ python names.py data/names.txt`

see `$ python names.py --help` for more info/options

## Testing
`$ PYTHONPATH=. pytest tests`