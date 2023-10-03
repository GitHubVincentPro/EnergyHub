# data/consumption.py

import pandas as pd

consumptions = pd.DataFrame({
'home1': [...],
'home2': [...]
})

consumptions.index = pd.date_range('1/1/2023', periods=100, freq='H')

consumptions.to_csv('consumption_data.csv')