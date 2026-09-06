import pandas as pd
import matplotlib.pyplot as plt
flight=pd.read_csv("flights.csv")
# print(flight)
departures=flight[["scheduled",'actual']]
# print(departures)
print(departures.info())
departures['scheduled'] = pd.to_datetime(departures['scheduled'])
departures['actual']=pd.to_datetime(departures['actual'])
# print(departures.info())
#calculated the delay
departures['delay']=departures.eval('actual-scheduled')
# print(departures)
departures['is_late']=departures['delay'].dt.total_seconds()>900
# print(departures)
departures['day_name']=departures['actual'].dt.strftime('%a')
# print(departures)
proportion_delayed=departures.groupby('day_name')['is_late'].mean()
percent_delayed=proportion_delayed*100
# print(percent_delayed)
new=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
percent_delayed=percent_delayed.reindex(new)
# print(percent_delayed)
import matplotlib.pyplot as plt
plt.bar(percent_delayed.index , percent_delayed)
plt.ylabel('Percentage of Delayed Flights')
plt.show()

#Project
import pandas as pd
color=pd.read_csv('emoji.csv')
# print(color.head())
# print(color.isna().sum())
color['sentiment'] = color['Pos [0...1]'] - color['Neg [0...1]']
# print(color.head())
color['postive_flag']=color['sentiment']> 0
# print(color.head())
percentage=color['postive_flag'].sum()/len(color)*100
top20=color.sort_values('Occurrences [5...max]',ascending = False).head(20)
# print(top20)
count=top20['postive_flag'].sum()/20*100
# print(count)
more=color['Occurences [5...max]'>500]
color=color[color['Occurences [5...max]']>500]
print(color)