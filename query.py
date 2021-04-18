import pandas as pd
import sqlite3
connexion=sqlite3.connect("factbook.db")

#cursor
c=connexion.cursor()
c.execute("select * from facts where population != ' ' order by population asc limit 10; ")

print(c.fetchall())
