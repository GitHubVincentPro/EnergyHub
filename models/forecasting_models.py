```python
# models/forecasting_models.py

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

class LSTMModel:

def __init__(self):
self.model = Sequential()
self.model.add(LSTM(50, input_shape=(lookback, 1)))
self.model.add(Dense(1))

def fit(self, x_train, y_train):
self.model.compile(optimizer='adam', loss='mse')
self.model.fit(x_train, y_train, epochs=100)

def predict(self, x_test):
return self.model.predict(x_test)

```

# Notebook d'entraînement du LSTM