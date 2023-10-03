```python
from keras.models import Sequential
from keras.layers import LSTM, Dense

def build_rnn():
model = Sequential()
model.add(LSTM(100, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(1))
return model

def train(model, X, y):
model.compile(optimizer='rmsprop', loss='mae')
model.fit(X, y, epochs=10)
```