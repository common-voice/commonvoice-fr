import pytest

from names import CustomFormatter


DEFAULT_DATA = dict(
    firstname='nicolas',
    lastname='panel',
    gender='monsieur',
)
CUSTOM_FORMATTER_TESTS = [
    ("{lastname}", DEFAULT_DATA, "panel"),
    ("{gender:capitalize}", DEFAULT_DATA, "Monsieur"),
    ("{firstname:capitalize_name}", DEFAULT_DATA, "Nicolas"),
    ("{firstname:capitalize_name}", dict(firstname='charles éric'), "Charles Éric"),
    ("{firstname:capitalize_name}", dict(firstname='charles-éric'), "Charles-Éric"),
    ("{firstname:spell_name}", DEFAULT_DATA, "N I C O L A S"),
    ("{firstname:spell_name}", dict(firstname='charles-éric'), "C H A R L E S plus loin É R I C"),
    ("{firstname:spell_name}", dict(firstname='pierre'), "P I E deux R E"),
]


@pytest.mark.parametrize('template, payload, expected', CUSTOM_FORMATTER_TESTS)
def test_custom_formatter(template, payload, expected):
    formatter = CustomFormatter()
    assert expected == formatter.format(template, **payload)