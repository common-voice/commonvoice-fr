import pytest
from bano import format_address


FORMAT_ADDRESS_TESTS = [
    (
        dict(number=37, street='Rue Berger', city='Le Havre', zipcode='76620'),
        '{number} {street_lower} à {city}',
        'trente-sept rue Berger au Havre',
    ),
    (
        dict(number='37C', street='Rue Berger', city='Le Havre', zipcode='76620'),
        '{number} {street_lower} à {city}',
        'trente-sept C rue Berger au Havre',
    ),
    (
        dict(number=37, street='Rue Berger', city='Le Havre', zipcode='76620'),
        '{zipcode}',
        'soixante-seize mille six cent vingt',
    ),
    (
        dict(number=37, street='Rue Berger', city='Le Havre', zipcode='76620'),
        '{zipcode_alt}',
        'soixante-seize, six cent vingt',
    ),
    (
        dict(number=37, street='Rue Berger', city='Paris', zipcode='75001'),
        '{zipcode}',
        'soixante-quinze mille un',
    ),
    (
        dict(number=37, street='Rue Berger', city='Paris', zipcode='75001'),
        ' {zipcode_alt} ',
        'soixante-quinze, zéro zéro un',
    ),
    (
        dict(number=37, street='Rue Berger', city='Paris', zipcode='75010'),
        '{zipcode_alt}',
        'soixante-quinze, zéro dix',
    ),
    (
        dict(number=37, street='Rue Berger', city='Paris', zipcode='01500'),
        '{zipcode}',
        'zéro un, cinq cents',
    ),
    (
        dict(number=37, street='Rue Berger', city='Paris', zipcode='01500'),
        '{zipcode}',
        'zéro un, cinq cents',
    ),
    (
        dict(number=37, street='Rue Berger', city='Paris', zipcode='05000'),
        '{zipcode}',
        'zéro cinq, zéro zéro zéro',
    ),
    (
        dict(number=37, street='Départementale 150', city='Les Milles', zipcode='13500'),
        '{street} à {city}',
        'Départementale cent cinquante aux Milles',
    ),
]


@pytest.mark.parametrize('address, template, expected', FORMAT_ADDRESS_TESTS)
def test_format_address(address, template, expected):
    assert expected == format_address(address=address, template=template)
