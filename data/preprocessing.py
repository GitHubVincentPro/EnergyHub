## data/preprocessing.py

```python
import pandas as pd

def preprocess_weather_data(file):
data = pd.read_csv(file)
data['datetime'] = pd.to_datetime(data['datetime'])
data = data.resample('H').mean()
return data
```
