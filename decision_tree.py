import pandas as pd

mb_file_path = '../input/train.csv'
mb_data = pd.read_csv(mb_file_path)
print(mb_data.columns)

price_data = mb_data.SalePrice
print(price_data.head())

cols = ['Lotsize','BuildingArea']
new_cols = mb_data[cols]