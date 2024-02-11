import sqlite3
import pandas as pd 
try:
    conn = sqlite3.connect('stats_can_immigrant.sqlite')

    # Complete Information Table - Population of Alberta 2021
    df = pd.read_csv('data/immigrants_alberta.csv')
    df.to_sql('immigrant', conn, if_exists='replace', index=False)

    # Population of Alberta by Continent
    df = pd.read_csv('data/immigrants_alberta_continent.csv')
    df.to_sql('immigrants_alberta_continent', conn, if_exists='replace', index=False)

    # Population of Alberta by Country
    df = pd.read_csv('data/immigrants_alberta_country.csv')
    df.to_sql('immigrants_alberta_country', conn, if_exists='replace', index=False)
except Exception as e:
    print (f'Error: {e}')
    print('Data not loaded')
else:
    print('By Continent')
    print(pd.read_sql('select * from immigrants_alberta_continent', conn))

    print('\nBy Country')
    print(pd.read_sql('select * from immigrants_alberta_country limit 10', conn))

    print('Immigrant data loaded')



