```python
from flask import Blueprint, request, jsonify
from core import predict, get_storage

api = Blueprint('api', '__name__')

@api.route('/forecast')
def forecast():
forecast = predict(request.json['data'])
return jsonify(forecast)

@api.route('/storage')
def storage():
status = get_storage()
return jsonify(status)
```