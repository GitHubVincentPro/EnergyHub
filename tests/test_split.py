
from data.processed import split
import unittest

class TestSplit(unittest.TestCase):

def test_train_test_split(self):
X_train,_,X_test = split.split_data()
self.assertNotEquals(X_train, X_test)