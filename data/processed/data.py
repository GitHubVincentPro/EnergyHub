import pandas as pd

class ProcessedData:

def __init__(self):
self.train = None
self.valid = None
self.test = None

def load_data(self):
# Charger les données
self.train = pd.read_csv('data/processed/train/data.csv')
self.valid = pd.read_csv('data/processed/valid/data.csv')
self.test = pd.read_csv('data/processed/test/data.csv')

def get_train(self):
return self.train

def get_valid(self):
return self.valid

def get_test(self):
return self.test

# data/processed/split.py

# Script de splitting
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('../interim/cleaned.csv')

X = data[['feat1','feat2']]
y = data['target']

X_train, X_rem, y_train, y_rem = train_test_split(X, y)
X_valid, X_test, y_valid, y_test = train_test_split(X_rem, y_rem)

# Sauver les données
X_train.to_csv('train/data.csv', index=False)
y_train.to_csv('train/target.csv', index=False)

# idem pour test et valid