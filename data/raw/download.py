
import requests

def download_data():
url = 'https://www.example.com/data.zip'
r = requests.get(url)
with open('data.zip', 'wb') as f:
f.write(r.content)

data/raw/extract.py

import zipfile
import pandas as pd

def extract_data():
with zipfile.ZipFile('data.zip') as zf:
zf.extract('data.csv')
df = pd.read_csv('data.csv')
return df

data/raw/check_quality.py

import pandas as pd

def check_data(df):
print(df.shape)
print(df.columns)
print(df.isnull().sum())
print(df.nunique())
# etc

# Tests

test/test_download.py
test/test_extract.py
test/test_check_quality.py