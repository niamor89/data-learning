import pytest

from m00_setup.stats_simples import moyenne


def test_moyenne_entiers():
    assert moyenne([1, 2, 3, 4]) == 2.5


def test_moyenne_un_seul_element():
    assert moyenne([7.0]) == 7.0


def test_moyenne_flottants():
    # Comparaison approchée: 0.1 + 0.2 n'est pas exactement 0.3 en flottant
    assert moyenne([0.1, 0.2]) == pytest.approx(0.15)


def test_moyenne_vide_leve_erreur():
    with pytest.raises(ValueError):
        moyenne([])
