import pandas as pd

data = pd.read_csv('customer_data.csv')
data.dropna(inplace=True)
