# Classe pour charger les données de manière transparente

class DataLoader:

def __init__(self):
self.data = None

def load_data(self):
if self.data is None:
# Charger les données
self.data = self._load_raw_data()
self.data = self._clean_data(self.data)
self.data = self._preprocess_data(self.data)

return self.data

def _load_raw_data(self):
# Charger les données brutes
return pd.read_csv('data/raw/...')

def _clean_data(self, data):
# Nettoyage
return data[[...]]

def _preprocess_data(self, data):
# Transformation
return data.groupby(...)

# data/validation.py

# Tests unitaires
import unittest
from loader import DataLoader

class TestDataLoader(unittest.TestCase):

def test_load_data(self):
loader = DataLoader()
data = loader.load_data()
self.assertEqual(data.shape, (1000,4))

# Main d'exemple
from loader import DataLoader

loader = DataLoader()
data = loader.load_data()

# Utiliser data...