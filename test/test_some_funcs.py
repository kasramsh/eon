from src.utils import plz_normalizer


def test_plz_normalizer():
    assert plz_normalizer('1478.0') == '01478'
