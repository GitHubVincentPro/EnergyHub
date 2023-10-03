# tests/test_models.py

import unittest
from models import forecast_model

class TestForecasting(unittest.TestCase):

def test_forecast_single_point(self):
forecast = forecast_model.predict(1)
self.assertEqual(forecast[0], 100) # Prévision attendue

def test_forecast_multiple_points(self):
forecasts = forecast_model.predict(5)
self.assertEqual(len(forecasts), 5)