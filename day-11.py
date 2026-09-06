import pandas as pd
word=pd.read_csv("animal.csv")
print(word)
#plottig trends
trend=word.query('word == "horse"')
print(trend)
# #plotting 
import matplotlib.pyplot as plt
plt.plot(trend['year'], trend['frequency'])
plt.ylabel('Frequency per million')
plt.title('Word frequency for "horse" over time')
plt.show()
def plot(animal):
    trend=word.query('word == @animal')
    plt.plot(trend['year'], trend['frequency'],label=animal)
plt.axvline(1886,color='black',ls='--')
plt.title('Frequency of the word over time')
plt.plot('penguin')
plt.plot('dinosaur')
plt.legend()
# plt.show()
plot('shrimp')
plt.axvline(1869,color='magenta',ls='--')
plt.title('Frequency of the word over time')  
plt.show()  