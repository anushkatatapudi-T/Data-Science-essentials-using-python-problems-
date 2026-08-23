import pandas as pd
df=pd.read_csv('right-angle.csv')
add=10
df["series"]=df["base"] + df["height"]
df['area']=0.5*df['base']*df['height']
df["minus"]=df['base']-df['height']
df['extra']=df['base']+add
print(df)

import pandas as pd
df=pd.read_csv('days.csv')
df=df.query('days>30')
print(df)

import pandas as pd
df=pd.read_csv('days.csv')
print(df)

import pandas as pd
df=pd.read_csv('days.csv')
df=df.query('days==days.min()')
print(df)

import pandas as pd
df=pd.read_csv('fruits.csv')
roups=df.groupby('fruit')
print(roups.size())

import pandas as pd
df=pd.read_csv('fruits.csv')
groups=df.groupby('fruit')
we=groups['weight'].mean()
print(we.reset_index())

#in a single line code
import pandas as pd
df=pd.read_csv('fruits.csv')
df=df.groupby('fruit')['weight'].mean().reset_index()
print(df)
