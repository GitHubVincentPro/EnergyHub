import pytest
from models import forecasting

@pytest.fixture
def solar_data():
# Charge les données solaires
return ...

@pytest.fixture
def rnn_model():
return forecasting.RNNForecaster()

class TestRNNForecasting:

def test_train(self, solar_data, rnn_model):

# Entraîne le modèle
rnn_model.train(solar_data)

# Valide que la loss diminue
losses = rnn_model.history['loss']
assert losses[-1] < losses[0]

def test_predict(self, solar_data, rnn_model):

# Prédit sur données de test
preds = rnn_model.predict(solar_data['test'])

# Vérifie qualité des prédictions
score = mean_absolute_error(preds, solar_data['test']['target'])
assert score < 0.1

class TestNaiveForecasting:

def test_predict(self, solar_data):

# Instancie modèle basique
model = forecasting.NaiveForecaster()

# Teste prédictions
preds = model.predict(solar_data['test'])
score = mean_absolute_error(preds, ...)
assert score < 0.2