Description des fichiers de données brutes :

- data.csv : données principales
- metadata.json : métadonnées

# data/raw/metadata.json

{
"columns": [
{
"name": "column1",
"type": "int",
"description": "Colonne 1"
},
{
"name": "column2",
"type": "string",
"description": "Colonne 2"
}
],
"source": "Lien vers la source des données",
"date": "Date de téléchargement"
}

# data/raw/import_data.py

# Script d'import
import pandas as pd

def import_data():
data = pd.read_csv('data.csv')

# Options de lecture
data = data.fillna('?')

return data

# Tests
import unittest
from import_data import import_data

class TestImport(unittest.TestCase):

def test_import(self):
data = import_data()
self.assertEqual(data.shape, (1000,10))