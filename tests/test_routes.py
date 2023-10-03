```python
import unittest
from api.core import predict
from api.models import ForecastRequest, ForecastResult

class TestCore(unittest.TestCase):

def setUp(self):
self.request = ForecastRequest(
date='2022-01-01',
location='Paris'
)

def test_predict_returns_result(self):
"""La fonction predict doit retourner un objet ForecastResult"""

result = predict(self.request)

self.assertIsInstance(result, ForecastResult)

def test_forecast_temperature(self):
"""Le champ temperature du résultat doit être un float"""

result = predict(self.request)

self.assertIsInstance(result.temperature, float)

def test_valid_forecast(self):
"""La prévision météo doit être une chaine valide"""

result = predict(self.request)

valid_forecasts = ['soleil', 'pluie', 'nuageux']

self.assertIn(result.weather, valid_forecasts)

if __name__ == '__main__':
unittest.main()
```