import sqlite3
import pandas as pd 
conn = sqlite3.connect('stats_can_immigrant.sqlite')

# Complete Information Table - Population of Alberta 2021
df = pd.read_csv('immigrants_alberta.csv')
df.to_sql('immigrant', conn, if_exists='replace', index=False)

# Population of Alberta by Continent
df = pd.read_csv('immigrants_alberta_continent.csv')
df.to_sql('immigrants_alberta_continent', conn, if_exists='replace', index=False)

# Population of Alberta by Country
df = pd.read_csv('immigrants_alberta_country.csv')
df.to_sql('immigrants_alberta_country', conn, if_exists='replace', index=False)

# Complete
# print(pd.read_sql('select * from immigrant', conn))

# Continent
# print(pd.read_sql('select * from immigrants_alberta_continent', conn))

# Country
# print(pd.read_sql('select * from immigrants_alberta_country', conn))



