import pandas as pd

a = pd.read_json('data.json')

print(a.to_string())
print(a.info())