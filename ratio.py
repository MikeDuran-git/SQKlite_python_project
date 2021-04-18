#objectif: Calculer le ratio de la surface terrestre totale sur la surface

# des océans totale appartenant aux pays de la table facts
 
  
import sqlite3
import pandas as pd
   
connexion = sqlite3.connect('factbook.db')

# On affiche dans un tableau pandas les sommes des surfaces terrestres et surfaces de l'eau pour chaque pays
a = pd.read_sql_query('SELECT SUM(area_land), SUM(area_water) FROM facts WHERE area_land != "";', con = connexion)

print(a)
      
# On affiche le ratio Terre / Mer
print(a['SUM(area_land)']/a['SUM(area_water)'])

