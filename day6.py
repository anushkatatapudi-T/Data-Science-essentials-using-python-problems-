import pandas as pd
df=pd.read_csv('art_data.csv')
feature=df.query('feature_id == "b104"')
# print(feature)
import pandas as pd
info=pd.read_csv('art_info.csv')
# print(info)
fea=pd.read_csv('feature.csv')
df=fea.groupby('painting_id').size()
# print(df)
comp=pd.read_csv('complex.csv')
# print(comp)
df=comp.groupby('painting_id').size()
# print(df)

#merging the data of info and complex
info=info.merge(comp,on='painting_id',how="left")
print(info)

import matplotlib.pyplot as plt
plt.figure(figsize=(6, 4))
plt.bar(info['year'], info['complexity'])
plt.xlabel('Year')
plt.ylabel('Complexity')
plt.show()