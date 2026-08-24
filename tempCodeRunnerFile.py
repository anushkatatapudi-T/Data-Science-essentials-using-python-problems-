import pandas as pd
import matplotlib.pyplot as plt
internet = pd.read_csv('world-internet-users.csv')
exceeds_100M = internet.query('internet_users > 100e6')
exceeds_100M.head(1)
print(internet)
print(exceeds_100M)
population = pd.read_csv('historical-world-population.csv')
df = internet.merge(population, on='year', how='left')
df = df.dropna()
print(df)