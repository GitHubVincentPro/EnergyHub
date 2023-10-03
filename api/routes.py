python
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


python
@api.route('/forecast')
def forecast():

try:
forecast = predict(request.json['data'])
return jsonify(forecast)

except Exception as e:
return jsonify({"error": str(e)}), 400

python
from schemas import ForecastSchema

@api.route('/forecast')
def forecast():

data = request.json

try:
ForecastSchema().load(data)

except ValidationError as e:
return jsonify(e.messages), 422

forecast = predict(data)
return jsonify(forecast)

python
@api.route('/simulation', methods=['POST'])
def simulation():

scenario = request.json

results = run_simulation(scenario)

return jsonify(results)