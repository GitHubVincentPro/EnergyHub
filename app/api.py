# app/api.py

from flask import Blueprint, request, jsonify
from models import forecast_model, battery_manager

api = Blueprint('api', __name__)

@api.route('/forecasts')
def get_forecasts():
forecasts = forecast_model.predict(24)
return jsonify(forecasts)

@api.route('/battery', methods=['POST'])
def control_battery():
data = request.get_json()
battery_manager.run_action(data['action'], data['amount'])
return jsonify(battery_manager.status())