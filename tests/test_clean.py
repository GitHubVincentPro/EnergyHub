import unittest
from data.interim import cleaning
import pandas as pd

class TestCleaning(unittest.TestCase):

def test_dropna(self):
df = cleaning.remove_na()
self.assertEqual(df.isna().sum().sum(), 0)

def test_column_transform(self):
df = cleaning.transform_column('col1', lambda x: x.upper())
self.assertTrue(df['col1'].str.isupper().all())