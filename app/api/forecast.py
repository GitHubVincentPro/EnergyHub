@forecast.route("/predict")
def predict():
# ...

@forecast.route("/simulations")
def simulate():
# ...

# app/api/storage.py

@storage.route("/status")
def status():
# ...

@storage.route("/charge", methods=['POST'])
def charge():
# ...

@storage.route("/discharge")
def discharge():
# ...

# tests/test_api.py

import app
import json

def test_predict():
client = app.create_app().test_client()

rv = client.get('/predict')
assert rv.status_code == 200
