### services.py

Service métier (gestion prévisions, stockage):

```python
from .models import Forecast

def get_forecasts():
# Récupérer prévisions de la BD
return [Forecast(datetime(...),...),...]
```