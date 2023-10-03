### routes.py

Implémenter les endpoints de l'API:

```python
from . import app

@app.route('/forecasts')
def get_forecasts():
# Renvoyer des prévisions

@app.route('/storage')
def get_storage_status():
# Renvoyer état du stockage
```