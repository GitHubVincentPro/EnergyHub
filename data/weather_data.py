```python
import pandas as pd

def load_weather_data():
solar = pd.read_csv('solar_data.csv')
temp = pd.read_csv('temp_data.csv')

# preprocess data
solar['datetime'] = pd.to_datetime(solar['datetime'])

return solar, temp
```