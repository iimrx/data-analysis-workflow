import pandas as pd

data = pd.read_csv('#')
data.fillna(0, inplace=True)
data.to_csv('#', index=False)
print(data.head())