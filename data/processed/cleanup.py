import pandas as pd

def clean_raw_data():
# Lire les données brutes
df = pd.read_csv('data/raw/myfile.csv')

# Traitements de nettoyage
df = df.dropna()
df['column'] = df['column'].apply(lambda x: x.strip())

# Enregistrer le résultat
df.to_csv('data/interim/cleaned_data.csv', index=False)

# data/transform.py

import pandas as pd

def preprocess_data():
df = pd.read_csv('data/interim/cleaned_data.csv')

# Créer de nouvelles colonnes
df['week'] = df['date'].dt.week

# Aggregation
df_agg = df.groupby('user_id').mean()

# Sauvegarder
df_agg.to_csv('data/processed/preprocessed_data.csv', index=True)

# data/split.py

from sklearn.model_selection import train_test_split

def split_train_test():
df = pd.read_csv('data/processed/preprocessed_data.csv')

X = df[['col1', 'col2']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y)

# Sauvegarder
X_train.to_csv('data/processed/train/X.csv')
y_train.to_csv('data/processed/train/y.csv')

X_test.to_csv('data/processed/test/X.csv')
y_test.to_csv('data/processed/test/y.csv')