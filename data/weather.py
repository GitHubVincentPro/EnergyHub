# data/weather.py

import pandas as pd

weather_data = pd.read_csv('weather_data.csv')

# Formater les données
weather_data['datetime'] = pd.to_datetime(weather_data['datetime'])
weather_data.set_index('datetime', inplace=True)

# Sauver le jeu de données formaté
weather_data.to_csv('weather_data_formatted.csv')