import sqlite3
import pandas as pd 
conn = sqlite3.connect('stats_can_population.sqlite')

print(pd.read_sql('SELECT GEO, MAX(VALUE) FROM population WHERE VALUE < (SELECT MAX(VALUE) FROM population)', conn))