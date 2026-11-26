"""Module de vérification de l'outillage: une fonction simple, typée et testée."""

from collections.abc import Sequence


def moyenne(valeurs: Sequence[float]) -> float:
    """Renvoie la moyenne arithmétique de `valeurs`.

    Lève ValueError si la séquence est vide, plutôt que de renvoyer 0 ou NaN:
    une moyenne d'un ensemble vide n'a pas de sens, autant échouer bruyamment.
    """
    if not valeurs:
        raise ValueError("moyenne() d'une séquence vide")
    return sum(valeurs) / len(valeurs)
