import sqlite3
import pandas as pd 
conn = sqlite3.connect('stats_can_immigrant_continent.sqlite')

df = pd.read_csv('immigrants_alberta_continent.csv')
df.to_sql('immigrant_continent', conn, if_exists='replace', index=False)

# print(pd.read_sql('select continent, max(population) from immigrant_continent', conn))