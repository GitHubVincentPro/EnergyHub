
import unittest
from data.raw import check_quality
import pandas as pd

class TestQuality(unittest.TestCase):

def test_column_names(self):
"""Vérifie les noms de colonnes"""
df = pd.DataFrame({'col1': [1,2], 'col2': [3,4]})
errors = check_quality.validate_columns(df)
self.assertEqual(errors, 0)

def test_row_count(self):
"""Vérifie le nombre de lignes"""
df = pd.DataFrame({'col1': [1,2]})
errors = check_quality.validate_row_count(df)
self.assertEqual(errors, 0)

def test_data_types(self):
"""Vérifie les types de données"""
df = pd.DataFrame({'col1': [1, '2']})
errors = check_quality.validate_types(df)
self.assertNotEqual(errors, 0)

def test_missing_values(self):
"""Vérifie les valeurs manquantes"""
df = pd.DataFrame({'col1': [1, None]})
errors = check_quality.check_missing(df)
self.assertNotEqual(errors, 0)