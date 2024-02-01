import sqlite3
import pandas as pd 
conn = sqlite3.connect('stats_can_population.sqlite')

df = pd.read_csv('population.csv', usecols=['GEO', 'VALUE'])
df.to_sql('population', conn, if_exists='replace', index=False)

# print(pd.read_sql('select * from population', conn))