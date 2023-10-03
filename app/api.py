Voici un exemple de code pour api.py qui ajouterait de nouvelles routes à l'API existante:

```python
# api.py

from flask import Flask, request, jsonify
from models import predict, predict_storage, run_simulation

app = Flask(__name__)

@app.route('/forecast')
def forecast():
# Route existante
pass

@app.route('/storage')
def predict_storage():

data = request.json
storage = predict_storage(data)
return jsonify(storage)

@app.route('/simulate', methods=['POST'])
def simulate():

scenario = request.json
result = run_simulation(scenario)
return jsonify(result)

@app.route('/status')
def status():

systems_status = get_system_status()
return jsonify(systems_status)

@app.route('/config')
def get_config():

config = load_config()
return jsonify(config)

if __name__ == '__main__':
app.run(debug=True)
```
