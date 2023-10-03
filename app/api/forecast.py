from flask import Blueprint, jsonify
from .models import ForecastModel
from .schemas import ForecastSchema

forecast_blueprint = Blueprint('forecast')

@forecast_blueprint.route("/forecast")
def get_forecast():
forecast = ForecastModel().predict()
serialized = ForecastSchema(many=True).dump(forecast)
return jsonify(serialized)