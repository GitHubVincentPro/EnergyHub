
from data.interim import transformation
import unittest

class TestTransformation(unittest.TestCase):

def test_new_column(self):
df = transformation.add_week_column()
self.assertIn('week', df.columns)

def test_aggregation(self):
df = transformation.group_by_user()
self.assertEqual(df.shape, (100,4))