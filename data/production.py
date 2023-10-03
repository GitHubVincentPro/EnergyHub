# data/production.py

import pandas as pd

solar_prod = pd.read_excel('solar_plant_production.xlsx')

solar_prod['datetime'] = pd.to_datetime(solar_prod['datetime'])

solar_prod.set_index('datetime', inplace=True)

solar_prod.to_csv('solar_production_data.csv')