# test_forecast_models.py
import pytest

from models import forecasting

@pytest.fixture
def solar_data():
# utiliser la fixture defined dans conftest
return pytest.solar_data

@pytest.fixture
def rnn_model():
return forecasting.RNNForecaster()

class TestRNNForecasting:

def test_train(self, solar_data, rnn_model):

# Entraîner le modèle
rnn_model.train(solar_data)

# Vérifier que la loss décroît
losses = rnn_model.history['loss']
assert losses[-1] < losses[0]

def test_predict(self, solar_data, rnn_model):

# Prédire sur des données de test
preds = rnn_model.predict(solar_data['test'])

# Vérifier la qualité des prédictions
score = mean_absolute_error(preds, solar_data['test']['target'])
assert score < 0.1

class TestNaiveForecasting:

def test_predict(self, solar_data):

# Instancier le modèle basique
model = forecasting.NaiveForecaster()

# Prédire et vérifier la qualité
preds = model.predict(solar_data['test'])
score = mean_absolute_error(preds, solar_data['test']['target'])
assert score < 0.2