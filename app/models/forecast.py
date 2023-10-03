import pandas as pd
from sklearn.ensemble import RandomForestRegressor

class ForecastModel:

def __init__(self):
self.model = RandomForestRegressor()

def train(self, X, y):
self.model.fit(X, y)

def predict(self, X):
return self.model.predict(X)

# Usage:

model = ForecastModel()
model.train(X_train, y_train)
forecast = model.predict(X_test)