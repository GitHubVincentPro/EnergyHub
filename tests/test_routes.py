python
import json
import unittest
from fastapi.testclient import TestClient
from api.main import app
from api.models import ForecastRequest, ForecastResult
from api.schemas import ForecastRequestSchema, ForecastResultSchema

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

def test_ forecast_response(self):
response = client.post("/forecast", json=self.valid_request)
data = json.loads(response.text)
result = ForecastResultSchema().load(data)
self.assertIsInstance(result, ForecastResult)

def test_invalid_json(self):
response = client.post("/forecast", json={"invalid": "data"})
self.assertEqual(response.status_code, 422)

def test_simulation_endpoint(self):
scenario = {"weather": "sunny"}
response = client.post("/simulation", json=scenario)
self.assertEqual(response.status_code, 200)

def test_not_found(self):
response = client.get("/unknown")
self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
unittest.main()