import pandas as pd

data = pd.read_csv('/home/liquidx/Desktop/sideProjecTs/datasets/gulf.csv')
data.fillna(0, inplace=True)
data.to_csv('/home/liquidx/Desktop/sideProjecTs/datasets/gulf.csv', index=False)
print(data.head())