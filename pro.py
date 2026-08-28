import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("largest-islands.csv")
p=df.head()
# print(p)
# import pandas as pd
# import matplotlib.pyplot as plt
# df=pd.read_csv('largest-islands.csv')
# land=df.query('island == "Yes"')
# top10=land.sort_values('rank').head(10)
# print(top10[["rank", "island", "area"]])
largest = df.sort_values("area", ascending=False).groupby("region").first()
# print(largest[["island", "area"]])
# import matplotlib.pyplot as plt
# data=df.sort_values('rank')
# plt.plot(data['rank'],data['area'],marker='o')
# plt.xlabel("Rank")
# plt.ylabel("Area")
# plt.title("AREA  VS  RANK ")
# plt.show()
multi = df[df["countries"].str.contains(",")]
print(multi[["island", "countries"]])