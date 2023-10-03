# Chargement des courbes de consommation

```python
# data/load_load_data.py

from sklearn.preprocessing import MinMaxScaler
import numpy as np

loads = pd.read_csv('loads/household_loads.csv')
scaler = MinMaxScaler()
scaled_loads = scaler.fit_transform(loads)

```