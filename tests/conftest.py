# conftest.py

import pytest
import pandas as pd

# Fixtures de données communes

@pytest.fixture
def solar_data():
return pd.read_csv("../data/solar_production.csv")

@pytest.fixture
def load_data():
return pd.read_csv("../data/load.csv")

@pytest.fixture
def prices_data():
return pd.read_csv("../data/prices.csv")

# Fixture de configuration

@pytest.fixture
def config():
return {
"api_url": "http://localhost:5000",
"data_path": "../data/"
}

# Autres fixtures utiles

@pytest.fixture
def client():
# Instancier un client d'API
return ApiClient()

@pytest.fixture
def forecast_model():
# Instancier un modèle pré-entraîné
return RNNForecast()