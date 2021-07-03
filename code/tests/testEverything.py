import pandas as pd

data = pd.read_csv('/home/liquidx/Desktop/sideProjecTs/datasets/gulf.csv')
data.drop('Unnamed: 0', axis=1, inplace=True)
data.to_csv('/home/liquidx/Desktop/sideProjecTs/datasets/gulf.csv')
print(len(data.columns))
print(data.columns)