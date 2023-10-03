```python
# Import des bibliothèques Keras et Tensorflow
from tensorflow import keras
from keras.models import Sequential
from keras.layers import LSTM, Dense

def lstm_model(input_dim, output_dim):

model = Sequential()
model.add(LSTM(100, input_shape=(input_dim,1)))
model.add(Dense(50, activation='relu'))
model.add(Dense(output_dim))

model.compile(loss='mse', optimizer='adam')
return model

def train_lstm(X_train, y_train, epochs=100):

model = lstm_model(X_train.shape[1], y_train.shape[1])

model.fit(X_train, y_train, epochs=epochs)

return model
```

### Dans notebooks/train_rnn_model.ipynb

```python
from models.forecasting_models import train_lstm

# Entraînement du modèle LSTM sur les données solaires
lstm_model = train_lstm(X_solar, y_solar)

# Évaluation sur le jeu de test
lstm_model.evaluate(X_test, y_test)
```