import pandas as pd
from sklearn.tree import DecisionTreeRegressor

mb_file_path = 'train.csv'
mb_data = pd.read_csv(mb_file_path)
mb_data = mb_data.dropna()
for index in mb_data.columns:
	print(index)

price_data = mb_data.SalePrice
print(price_data.head())

cols = ['Rooms','Price']
new_cols = mb_data[cols]
print(new_cols)
#print(new_cols.describe())

# choosing a Prediction Target
y = mb_data.Price

# choosing predictors 
melbourne_predictors = ['Rooms','Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt',
'Lattitude', 'Longtitude']
X = mb_data[melbourne_predictors]

# define model
melbourne_model = DecisionTreeRegressor()

# fit model
melbourne_model.fit(X, y)

# making predictions
print("Making predictions for the following 5 houses...\n")
print(X.head())
print("The predictions are\n")
print(melbourne_model.predict(X.head()))