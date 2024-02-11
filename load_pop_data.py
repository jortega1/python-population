import sqlite3
import pandas as pd 
try:
    conn = sqlite3.connect('stats_can_population.sqlite')

    df = pd.read_csv('data/population.csv', usecols=['GEO', 'VALUE'])
    df.to_sql('population', conn, if_exists='replace', index=False)

    sql = pd.read_sql('select * from population limit 10', conn)
except Exception as e:
    print (f'Error: {e}')
    print('Data not loaded')
else :
    print (sql)
    print('Population data loaded')
