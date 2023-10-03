```python
from keras.models import Sequential
from keras.layers import LSTM, GRU, Conv1D, Dense

def build_rnn_model():

model = Sequential()
model.add(LSTM(100, input_shape=(x_train.shape[1],x_train.shape[2])))
model.add(Dense(1))
return model

def build_cnn_model():

model = Sequential()
model.add(Conv1D(64, 5, activation='relu',
input_shape=(x_train.shape[1],x_train.shape[2])))
model.add(Conv1D(32, 5, activation='relu'))
model.add(Dense(1))
return model

```