```python
# app/api.py

@app.route('/predict')
def predict():
data = request.json
forecast = LSTMModel().predict(data)
return jsonify(forecast)
```
