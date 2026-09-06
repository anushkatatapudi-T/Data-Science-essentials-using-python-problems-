import pandas as pd
data=pd.read_csv('coffee.csv')
print(data)
print(data.columns)
needed_columns = [
    'How many cups of coffee do you typically drink per day?',
    'Where do you typically drink coffee?',
    'Where do you typically drink coffee? (At home)',
    'Where do you typically drink coffee? (At the office)',
    'Where do you typically drink coffee? (On the go)',
    'Where do you typically drink coffee? (At a cafe)',
    'Where do you typically drink coffee? (None of these)',
    'How do you brew coffee at home?'
]
dairy = data[needed_columns]
print(dairy)
name_map = {
    'How many cups of coffee do you typically drink per day?':'2cups',
    'Where do you typically drink coffee?':'Home',
    'Where do you typically drink coffee? (At home)':"Home(coffee)",
    'Where do you typically drink coffee? (At the office)':'Office',
    'Where do you typically drink coffee? (On the go)':'Outside',
    'Where do you typically drink coffee? (At a cafe)':'Cafe',
    'Where do you typically drink coffee? (None of these)':'NOne',
    'How do you brew coffee at home?':'Creamer',
}
print('hi'*2)