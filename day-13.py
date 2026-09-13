import pandas as pd
import matplotlib.pyplot as plt
df_public=pd.read_csv('healthy')
print(df_public)
#food and public
df_public['public']=df_public.eval('yes / (yes+no+no_opinion)')
df_public['public']=df_public.eval('public * 100').round()
print(df_public)
df_public=df_public[['food','public']]
print(df_public)
#experts and food
df_experts=pd.read_csv('experts')
df_experts['experts']=df_experts.eval('yes / (yes +no + no_opinion)')
df_experts['experts']=df_experts.evel('experts * 100').round()
df_experts=df_experts[['food','experts']]
print(df_experts)
#merging
df=df_public.merge(df_experts, on ='food',how='left')
print(df)
#plotting
import matplotlib.pyplot as plt
plt.scatter(df['public'],df['experts'])
plt.xlabel('public (%)')
plt.ylabel('experts(%)')
plt.title("IS FOOD IS HEALTHY")