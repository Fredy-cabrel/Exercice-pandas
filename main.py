import pandas as pd
import numpy as np

# series : tableau uni-dimensionnel avec un index tres explicite 
# (équivalent d'une colonne dans un dataframe), il prends encompte 
# 2 parametres : le premier est un tableau ou une liste python et 
# le deuxieme c'est les index

# dataframe : structure données bi-dimensionnel qui semblable a un 
# tableau excel avec des lignes et des colonnes, tous les fichiers 
# importés seront représenté sous forme de dataframe pandas pour faciliter la manipulation

a = pd.Series([10, 45, 88], index = ["a", "b", "c"])
print(a)


data = {
    'Noms' : ["Fredy", "Cabrel", "Michel", "steve", "Nathan"],
    'age' : [21, 24, 20, 16, 7],
    'sexe' : ["M", "F", "M", "F", "M"]
}

data2 = {
    'Noms' : ["Fredy", "Cabrel", "Michel", "steve", "Nathan"],
    'salaire' : [210000, 240000, 200000, 160000, 70000],
    'sexe' : ["M", "F", "M", "F", "M"]
}

df = pd.DataFrame(data) # ici chaque colonne est une serie, serie avec index 0 et l'autre serie avec index 1 
print(df)

df2 = pd.DataFrame(data2) # ici chaque colonne est une serie, serie avec index 0 et l'autre serie avec index 1 
print(df2)

df_merged = pd.merge(df, df2.loc[:, ["Noms","salaire"]], on="Noms", how="left")
print(df_merged)

