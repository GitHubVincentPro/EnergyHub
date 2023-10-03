# Importation des données météo

```python
# data/load_weather_data.py

import pandas as pd

solar_france = pd.read_csv('weather/solar_france.csv')
temp_france = pd.read_csv('weather/temp_france.csv')

```