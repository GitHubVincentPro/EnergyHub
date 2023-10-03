python
import pandas as pd

def load_weather_data():
df = pd.read_csv('weather_data.csv')
return df

def load_solar_production():
df = pd.read_csv('solar_farm_production.csv')
return df

def load_customer_load():
dfs = {}
for customer in CUSTOMERS:
dfs[customer] = pd.read_csv(f'customer_{customer}_load.csv')
return dfs