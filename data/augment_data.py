# Simulation de données manquantes

```python
# data/augment_data.py

import random

def insert_missing_values(data):
n_miss = int(len(data) * 0.1)
idxs = random.sample(range(len(data)), n_miss)

for i in idxs:
data.loc[i] = np.nan

return data
```