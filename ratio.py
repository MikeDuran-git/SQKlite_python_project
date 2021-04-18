#objectif: Calculer le ratio de la surface terrestre totale sur la surface

# des océans totale appartenant aux pays de la table facts
 
  
import sqlite3
import pandas as pd
import math
connexion = sqlite3.connect('factbook.db')

# On affiche dans un tableau pandas les sommes des surfaces terrestres et surfaces de l'eau pour chaque pays
a = pd.read_sql_query('SELECT SUM(area_land), SUM(area_water) FROM facts WHERE area_land != "";', con = connexion)

print(a)
      
# On affiche le ratio Terre / Mer
print(a['SUM(area_land)']/a['SUM(area_water)'])

print("-------------------------")

#Quelles pays ont eus le plus d'immigrants ?
b1=pd.read_sql_query("select name, area, area_land, migration_rate from facts where migration_rate in (select max(migration_rate) from facts);",con=connexion)
print(b1)
print("-------------------------")

b2=pd.read_sql_query("select name, area, area_land, migration_rate from facts where migration_rate in (select min(migration_rate) from facts);",con=connexion)
print(b2)
print("-------------------------")

def pop_growth(x):
     return x['population'] * math.e ** ((x['population_growth']/100)* 35)
 
def density(x):
    return x['population']/x['area']


a = pd.read_sql_query('SELECT * FROM facts WHERE area != "" and area != "0"', con = connexion)
 
# Application de la fonction pop_growth à chaque pays + création d'une colonne pop_2050 contenant les résultats
a['pop_2050'] = a.apply(lambda row: pop_growth(row), axis=1)

a['density']= a.apply(lambda row: density(row), axis=1)
 
# Suppression des lignes contenant des valeurs manquantes
a = a.dropna(axis = 0)
  
 
# On trie les pays par population décroissante
b = a.sort_values(['density'], ascending = [False])
 
print(b)