### models.py

Modèles de données (Forecast, StorageUnit etc):

```python
from datetime import datetime

class Forecast:
def __init__(self, date, value):
self.date = date
self.value = value
```