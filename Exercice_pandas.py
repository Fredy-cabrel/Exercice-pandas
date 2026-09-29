import pandas as pd

# Niveau 1 : Créer un DataFrame
data = {
    "nom" : ["Alice", "Bob", "Claire"],
    "age" : [22, 25, 20]
}

df = pd.DataFrame(data)

# 1. Afficher le DataFrame.
print(df)

# 2. Afficher les colonnes.
print(df.columns)

# 3. Afficher les 2 premières lignes.
print(df.head(2))
# ou
# print(df[0:2])
# ou
# print(df.loc[0:1])
# ou
# print(df.iloc[0:2])

# 4. Afficher le nombre total de lignes.
print(len(df))


# Niveau 2 : Sélection de colonnes
data = {
    "nom": ["Alice", "Bob", "Claire"],
    "age": [22, 25, 20],
    "ville": ["Paris", "Lyon", "Marseille"]
}

# 1. Afficher uniquement la colonne age.
df = pd.DataFrame(data)
print(df.loc[:,"age"])
# ou 
# df["age"]

# 2. Afficher nom et ville.
print(df.loc[:, ["nom", "ville"]])
# ou 
# df[["nom", "ville"]]

# 3. Afficher la valeur située ligne 1 colonne ville.
print(df.loc[1, "ville"])


# Niveau 3 : Filtrage
data = {
    "nom": ["Alice", "Bob", "Claire", "David"],
    "age": [22, 25, 20, 30]
}

df = pd.DataFrame(data)

# 1. Afficher les personnes de plus de 22 ans.
cond_plus_22 = df["age"] > 22
pers_plus_22 = df[cond_plus_22]
print(pers_plus_22)

# 2. Afficher les personnes de moins de 25 ans.
cond_moins_25 = df["age"] < 25
pers_moins_25 = df[cond_moins_25]
print(pers_moins_25)

# 3. Afficher la personne âgée de 30 ans.
cond_30 = df["age"] == 30
pers_30 = df[cond_30]
print(pers_30)


# Niveau 4 : Statistiques
data = {
    "note": [12, 15, 10, 18, 20]
}

df = pd.DataFrame(data)

# 1. Moyenne des notes.
moy_note = df["note"].mean()
print(moy_note)

# 2. Maximum.
max_note = df["note"].max()
print(max_note)

# 3. Minimum.
min_note = df["note"].min()
print(min_note)

# 4. Écart-type.
std_note = df["note"].std()
print(std_note)


# Niveau 5 : Trier les données
data = {
    "nom": ["Alice", "Bob", "Claire", "David"],
    "salaire": [2500, 4000, 3000, 1500]
}

df = pd.DataFrame(data)

# 1. Trier par salaire croissant.
df_asc = df.sort_values(by="salaire")
print(df_asc)

# 2. Trier par salaire décroissant.
df_desc = df.sort_values(by="salaire", ascending=False)
print(df_desc)

# 3. Trouver le salaire le plus élevé.
salaire_max = df["salaire"].max()
print(salaire_max)


# Niveau 6 : Création de colonnes
data = {
    "nom": ["Alice", "Bob", "Claire"],
    "salaire": [2500, 4000, 3000]
}

df = pd.DataFrame(data)

# 1. Créer une colonne prime = salaire × 0.10.
# def mul(x: float):
    # return x * 0.10
# df["prime"] = df["salaire"].apply(mul)
# print(df)

df["prime"] = df["salaire"] * 0.10
print(df)

# 2. Créer une colonne salaire_total.
df["salaire_total"] = df["salaire"] + df["prime"]
print(df)


# Niveau 7 : GroupBy
data = {
    "service": ["IT", "IT", "RH", "RH", "Finance"],
    "salaire": [3000, 3500, 2500, 2700, 4000]
}

df = pd.DataFrame(data)

# 1. Salaire moyen par service.
df_sal_moy = df.groupby('service')[["salaire"]].mean()
print(df_sal_moy)

# 2. Salaire max par service.
df_sal_max = df.groupby('service')[["salaire"]].max()
print(df_sal_max)

# 3. Nombre d'employés par service.
df_empl = df.groupby('service').size()
print(df_empl)


# Niveau 8 : Jointures
employes = pd.DataFrame({
    "id": [1, 2, 3],
    "nom": ["Alice", "Bob", "Claire"]
})

salaires = pd.DataFrame({
    "id": [1, 2, 3],
    "salaire": [3000, 4000, 3500]
})

# 1. Fusionner les deux tables.
df_merge = pd.merge(employes, salaires, on="id", how="left")
print(df_merge)

# 2. Afficher nom et salaire.
df_ns = df_merge[["nom", "salaire"]]
print(df_ns)

# 3. Trouver l'employé le mieux payé.
df_empl_pay = df_merge.loc[df_merge["salaire"].idxmax()]
print(df_empl_pay)


# Niveau 9 : Valeurs manquantes
data = {
    "nom": ["Alice", "Bob", None, "David"],
    "age": [22, None, 30, 25]
}

df = pd.DataFrame(data)

# 1. Compter les valeurs manquantes.
print(df.isna().sum())

# 2. Remplacer les âges manquants par la moyenne.
print(df["age"].fillna(df["age"].mean()))

# 3. Supprimer les lignes contenant des valeurs manquantes.
print(df.dropna())


# Niveau 10 : Projet complet
data = {
    "nom": ["Alice", "Bob", "Claire", "David", "Emma"],
    "service": ["IT", "RH", "IT", "Finance", "RH"],
    "salaire": [3000, 2500, 3500, 5000, 2700],
    "anciennete": [2, 5, 1, 10, 3]
}

df = pd.DataFrame(data)

# Défis
# 1. Afficher l'employé le mieux payé.
mieux_paye = df.loc[df["salaire"].idxmax()]
print(mieux_paye)
# 2. Afficher le salaire moyen par service.
df_sal_moy_serv = df.groupby('service')[["salaire"]].mean()
print(df_sal_moy_serv)
# 3. Ajouter une colonne prime = 5% du salaire.
df["prime"] = df["salaire"] * 0.05
print(df)
# 4. Afficher les employés ayant plus de 3 ans d'ancienneté.
plus_3ans = df["anciennete"] > 3
print(df[plus_3ans])
# 5. Trier du salaire le plus élevé au plus bas.
df_trier_élévé_bas = df.sort_values(by="salaire", ascending=False)
print(df_trier_élévé_bas)
# 6. Afficher les 3 meilleurs salaires.
df_3_meil_sal = df_trier_élévé_bas.head(3)
print(df_3_meil_sal)
# 7. Quel service paie le plus en moyenne ?
paie_plus_moy = df_sal_moy_serv.idxmax()
print(paie_plus_moy)



# Niveau Boss Final

data = {
    "date": [
        "2024-01-01",
        "2024-01-01",
        "2024-01-02",
        "2024-01-02",
        "2024-01-03"
    ],
    "programme": [
        "INFO",
        "INFO",
        "MATH",
        "INFO",
        "MATH"
    ],
    "lettres": [10, 15, 7, 20, 5]
}

df = pd.DataFrame(data)

# 1. Total des lettres par jour.
df_tot_let_jour = df.groupby('date')["lettres"].sum()
print(df_tot_let_jour)
# 2. Total des lettres par programme.
df_tot_let_prog = df.groupby('programme')["lettres"].sum()
print(df_tot_let_prog)
# 3. Total par jour et programme.
df_tot_let_jour_prog = df.groupby(['date', 'programme'])["lettres"].sum()
print(df_tot_let_jour_prog)
# 4. Jour avec le plus de lettres.
df_plus_let_jour = df_tot_let_jour.idxmax()
print(df_plus_let_jour)
# 5. Programme avec le plus de lettres.
df_plus_let_prog = df_tot_let_prog.idxmax()
print(df_plus_let_prog)
# 6. Moyenne des lettres par jour.
df_moy_let_jour = df.groupby('date')["lettres"].mean()
print(df_moy_let_jour)
# 7. Convertir la colonne date en datetime.
df["date"] = pd.to_datetime(df["date"])
print(df)
print(df.dtypes)
# 8. Trier par date décroissante.
trie_dat_desc = df.sort_values(by="date", ascending=False)
print(trie_dat_desc)
# 9. Créer une colonne cumul_lettres.
df["cumul_lettres"] = df["lettres"].cumsum()
print(df)
# 10. Afficher uniquement les jours où plus de 20 lettres ont été envoyées.
df_jour_sup_20 = df_tot_let_jour > 20
print(df_tot_let_jour[df_jour_sup_20])

