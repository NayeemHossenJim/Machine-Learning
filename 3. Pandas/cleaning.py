import pandas as pd
a = pd.read_csv('data.csv')
#a['Calories'].fillna(200,inplace=True)
a.dropna(inplace=True)
print(a['Calories'].mean())
print(a['Calories'].median())
print(a['Calories'].mode())
print(a.corr())

