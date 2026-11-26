# m00_setup

Vérifier que la chaîne complète fonctionne avant d'écrire du vrai code d'apprentissage: environnement virtuel, ruff, pytest, CI GitHub Actions, workflow branche puis pull request.

## Ce que j'en retiens

- Les dossiers de modules sont nommés `mNN_sujet` et pas `NN-sujet`: un nom Python ne peut ni commencer par un chiffre ni contenir de tiret, sinon les tests ne peuvent pas l'importer.
- `pytest.approx` sert à comparer des flottants, car `0.1 + 0.2 != 0.3` en binaire.
- Une fonction qui reçoit une entrée invalide lève une exception explicite plutôt que de renvoyer une valeur trompeuse.

## Lancer

```bash
pytest m00_setup
```
