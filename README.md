# data-learning

Mes notes, exercices et projets de reconversion vers la data et l'IA, en préparation puis pendant le bootcamp Data Science & IA du Wagon Paris (18 janvier-19 mars 2027).

## Règle de contenu

Ce dépôt est public. Il contient uniquement mes notes personnelles et mes propres projets. Aucun énoncé ni corrigé du Wagon n'y est publié.

## Organisation

Un dossier par module, nommé `mNN_sujet` (nom valide en Python, donc importable par les tests). Chaque module contient:

- `README.md`: ce que j'ai appris, en mes mots
- le code (`*.py`), typé et conforme PEP 8
- les tests (`test_*.py`) exécutés par pytest

| Module | Sujet | Statut |
|---|---|---|
| [m00_setup](m00_setup/) | Outillage, premier test | en cours |

## Lancer en local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
ruff check .
ruff format --check .
pytest
```

## Workflow

Une branche par exercice, une pull request, la CI GitHub Actions (ruff + pytest) doit passer avant fusion.
