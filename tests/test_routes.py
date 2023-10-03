```python
import json
import unittest
from fastapi.testclient import TestClient

from api.main import app
from api.models import ForecastRequest, ForecastResult
from api.schemas import ForecastRequestSchema

client = TestClient(app)

class TestRoutes(unittest.TestCase):

def setUp(self):
self.valid_request = {
"date": "2023-01-01",
"location": "Paris"
}

def test_forecast_endpoint(self):
response = client.post("/forecast", json=self.valid_request)
self.assertEqual(response.status_code, 200)

def test_valid_request(self):
response = client.post("/forecast", json=self.valid_request)
data = response.json()
ForecastRequestSchema().validate(data)

def test_invalid_json(self):
response = client.post("/forecast", json={"invalid": "data"})
self.assertEqual(response.status_code, 422)

def test_missing_parameter(self):
request = {"location": "Paris"}
response = client.post("/forecast", json=request)
self.assertEqual(response.status_code, 422)

def test_not_found(self):
response = client.get("/unknown")
self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
unittest.main()
```