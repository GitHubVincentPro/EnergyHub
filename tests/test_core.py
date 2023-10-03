```python
import unittest
from api.core import predict
from api.models import ForecastRequest, ForecastResult

class TestCore(unittest.TestCase):

def setUp(self):
self.request = ForecastRequest(
date="2022-01-01",
location="Paris"
)

def test_predict_returns_result(self):
result = predict(self.request)
self.assertIsInstance(result, ForecastResult)

def test_forecast_temperature(self):
result = predict(self.request)
self.assertIsInstance(result.temperature, float)

def test_valid_weather(self):
possible_weather = ['sunny', 'rainy', 'cloudy']
result = predict(self.request)
self.assertIn(result.weather, possible_weather)

def test_empty_request(self):
request = ForecastRequest()
self.assertRaises(Exception, predict, request)

def test_invalid_location(self):
request = ForecastRequest(location="Invalid")
self.assertRaises(Exception, predict, request)

if __name__ == '__main__':
unittest.main()
```
