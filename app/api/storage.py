from flask import Blueprint, jsonify
from .models import BatteryModel
from .schemas import BatteryStatusSchema, ChargeCommandSchema

storage_blueprint = Blueprint('storage')

@storage_blueprint.route("/status")
def get_status():
status = BatteryModel().get_status()
serialized = BatteryStatusSchema().dump(status)
return jsonify(serialized)

@storage_blueprint.route("/charge", methods=['POST'])
def charge():
data = ChargeCommandSchema().load(request.get_json())
BatteryModel().charge(data)
return "OK", 201