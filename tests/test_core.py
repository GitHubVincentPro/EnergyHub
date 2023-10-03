```python
import unittest
from api.core import predict
from api.models import ForecastRequest, ForecastResult

class TestCore(unittest.TestCase):

def setUp(self):

# Requête valide
self.valid_request = ForecastRequest(
date="2023-01-01",
location="Paris"
)

# Données de prédiction
self.forecast_data = {
"temperature": 15,
"weather": "Sunny"
}

def test_valid_forecast(self):

result = predict(self.valid_request)

self.assertEqual(result.temperature, self.forecast_data["temperature"])
self.assertEqual(result.weather, self.forecast_data["weather"])

def test_invalid_location(self):

invalid_request = ForecastRequest(location="Unknown")

with self.assertRaises(ValueError):
predict(invalid_request)

def test_forecast_types(self):

result = predict(self.valid_request)

self.assertIsInstance(result.temperature, float)
self.assertIsInstance(result, ForecastResult)

def test_mock_prediction(self):

# Mock la fonction de prédiction
def mock_predict(request):
return ForecastResult(**self.forecast_data)

predict = mock_predict

result = predict(self.valid_request)

self.assertEqual(result.temperature, 15)

if __name__ == '__main__':
unittest.main()
```