# # import pandas as pd
# # import matplotlib.pyplot as plt
# # internet=pd.read_csv('extension-internet-users-by-continent.csv')
# # print(internet)

# #task
# # import pandas as pd
# # internet=pd.read_csv('extension-internet-users-by-continent.csv')
# # population=pd.read_csv("extension-historical-population-by-continent.csv")
# # print(population)

# #task : exceed - 100
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # internet=pd.read_csv('extension-internet-users-by-continent.csv')
# # exc=internet.query('internet_users > 50e6')
# # print(exc)

# #merge the data
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # internet=pd.read_csv('extension-internet-users-by-continent.csv')
# # population=pd.read_csv("extension-historical-population-by-continent.csv")
# # df=internet.merge(population,on='year',how='left')
# # df.dropna()
# # print(df)

# #task 
# import pandas as pd
# import matplotlib.pyplot as plt
# internet=pd.read_csv('extension-internet-users-by-continent.csv')
# population=pd.read_csv("extension-historical-population-by-continent.csv")
# df=internet.merge(population,on='year',how='left')
# # 

# #plotting the graph
# import matplotlib.pyplot as plt
# plt.plot(df['year'], df['percent'])
# plt.axhline(50, color='gray', linestyle='--')
# plt.xlabel('Year')
# plt.ylabel('Percent Connected')
# plt.show()

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
df['percent'] = df.eval('internet_users/population * 100')
df['percent'] = df['percent'].round(2)
import matplotlib.pyplot as plt
plt.plot(df['year'], df['percent'])
plt.axhline(50, color='gray', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Percent Connected')
plt.title("Percentage of Increase of World")
plt.show()
