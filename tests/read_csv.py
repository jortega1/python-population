import pandas
df = pandas.read_csv('population.csv', usecols=['GEO', 'VALUE'], header=0)
#df.to_csv(header=None);
print(df.to_csv(header=None))

