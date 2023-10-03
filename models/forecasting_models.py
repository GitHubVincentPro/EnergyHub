import pandas as pd
from sklearn.linear_model import LinearRegression

def train_linear_regression(X, y):

lr = LinearRegression()
lr.fit(X, y)
return lr

def forecast_consumption(lr_model, new_data):

X_new = new_data[['weather', 'hour']]
return lr_model.predict(X_new)