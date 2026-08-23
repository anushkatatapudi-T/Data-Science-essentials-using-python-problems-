
import pandas as pd
df=pd.read_csv('adult-human-skeleton.csv')
df.query('head == "region"')
print(df)