# Exercice-pandas

# Cours Pandas

Un espace d'apprentissage pour pratiquer Python et la bibliothèque Pandas à travers des exemples progressifs et des exercices.

## Contenu du dossier

| Fichier | Contenu |
|---|---|
| `main.py` | Séries et DataFrames, fusion de tables avec `merge`, exemples avec des données de personnes. |
| `Exercice_pandas.py` | Exercices progressifs : sélection, filtrage, statistiques, tri, colonnes, `groupby`, jointures et valeurs manquantes. Comprend aussi un projet récapitulatif sur des données de lettres. |
| `Exercices_avances.py` | Analyses par groupe, taux d'acceptation, agrégations, sommes cumulées, classements et différents types de jointures. |
| `data.csv` | Petit exemple de données avec les colonnes `Noms`, `age` et `sexe`. |

## Prérequis

- Python 3
- Pandas
- NumPy (utilisé dans `main.py`)

## Installation avec `venv` (Windows PowerShell)

Depuis le dossier du projet :

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pandas numpy
```

Pour quitter l'environnement virtuel :

```powershell
deactivate
```

## Lancer les scripts

Avec l'environnement virtuel activé :

```powershell
python main.py
python Exercice_pandas.py
python Exercices_avances.py
```

Ou directement avec le lanceur Python Windows, si les dépendances sont installées dans l'environnement utilisé par `py` :

```powershell
py main.py
py Exercice_pandas.py
py Exercices_avances.py
```

## Notions pratiquées

- Créer et afficher une `Series` et un `DataFrame`.
- Sélectionner des lignes et des colonnes avec `loc` et `iloc`.
- Filtrer des lignes avec des conditions.
- Calculer des statistiques et traiter des valeurs manquantes.
- Trier les données et créer des colonnes calculées.
- Regrouper et agréger les données avec `groupby`.
- Fusionner des tables avec `merge`.
- Manipuler des dates, calculer des sommes cumulées et créer des classements.

## Environnements Python : `venv` et Poetry

`venv` crée un environnement virtuel Python. Poetry peut aussi gérer cet environnement, ainsi que les dépendances et leurs versions dans `pyproject.toml` et `poetry.lock`.

Pour initialiser Poetry et ajouter les bibliothèques du cours :

```powershell
poetry init
poetry add pandas numpy
poetry run python main.py
```
