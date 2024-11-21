import pandas as pd

a = pd.read_csv('data.csv')

print(a.to_string())
print(pd.options.display.max_rows)