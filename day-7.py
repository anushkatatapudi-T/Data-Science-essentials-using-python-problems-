import pandas as pd
df=pd.read_csv('songs.csv')
print(df)
df=df.query('duration == duration.min()')
print(df.head(5))
import matplotlib.pyplot as plt
plt.plot(df['year'] , df['duration'])
plt.xlabel("Year")
plt.ylabel("Duration")
plt.show()
print(df.info)
s=df['duration'].str.split(':',expand=True)
s=s.astype(int)
df[['h','m','s']]=s
df['total_seconds']=df.eval('h*3600 + m*60 + s')
print(df)
import matplotlib.pyplot as plt
plt.plot(df['year'],df['total_seconds'])
plt.xlabel('Year')
plt.ylabel("Total seconds")
plt.show()
