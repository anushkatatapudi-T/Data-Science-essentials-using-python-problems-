import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("deepest.csv")
cat=df['category'].value_counts()
print(cat)
Max_depth=df.groupby('category')['depth'].max()
print(max)
dd=Max_depth.reset_index(name='Max_depth')
dd=dd.sort_values('Max_depth')
print(dd)
import matplotlib.pyplot as plt
plt.barh(dd['category'],dd['Max_depth'])
plt.xlabel("Max Depth of each category")
plt.show()
def Clear_axes():
    ax=plt.gca()#gca is to show the present graph 
    ax.spines(['top','down','left','right']).set_visible(False)#spines are for a graph box and set_visible means to make the line invisible
    ax.grid(axis='x',color='black',alpha=0.5)#grid means add grid line,aplha transparency
    ax.tick_params(axis='both',lenght=0)#to maintain the tick
# plt.show()
dd['color'] = 'C0'
dd.loc['ref_0'] = ['submarine implosion', 730, 'C1']
dd = dd.sort_values('Max_depth')
print(dd)
import matplotlib.pyplot as plt
plt.barh(dd['category'],dd['Max_depth'],dd['color'])
plt.xlabel("Max Depth of each category")
plt.show()






