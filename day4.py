import pandas as pd
df=pd.read_csv('adult-human-skeleton.csv')
print(df)

import pandas as pd
df=pd.read_csv('adult-human-skeleton.csv')
df=df['region'].value_counts()
print(df)

import pandas as pd
df=pd.read_csv('adult-human-skeleton.csv')
df=df.sort_values(by ='fused_from', ascending= False)
print(df)

import pandas as pd
df=pd.read_csv('adult-human-skeleton.csv')
df.query('head == "region"')
print(df)

import pandas as pd
mammal=pd.read_csv('mammal-neck-bones.csv')
print(mammal)

import pandas as pd
mammal=pd.read_csv('mammal-neck-bones.csv')
print(mammal.query('neck_vertebrae != 7'))


import pandas as pd
bird=pd.read_csv('bird-neck-bones.csv')
print(bird)

import pandas as pd
import matplotlib.pyplot as plt
bird=pd.read_csv('bird-neck-bones.csv')
bird_count= bird['neck_vertebrae'].value_counts().sort_index()
print(bird_count.plot.bar())
plt.ylabel('count')
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
bird=pd.read_csv('bird-neck-bones.csv')
bird = bird.query('neck_vertebrae == neck_vertebrae.max()')
print(bird)