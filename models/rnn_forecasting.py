```python
from keras.models import Sequential
from keras.layers import LSTM, Dense

def build_rnn_model():
model = Sequential()
model.add(LSTM(100, input_shape=(lookback,1)))
model.add(Dense(1))
model.compile(loss='mse')
return model

def train_rnn(X, y):
model.fit(X, y, epochs=100)
```