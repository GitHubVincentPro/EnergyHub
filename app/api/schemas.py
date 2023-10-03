from marshmallow import Schema, fields

class ForecastSchema(Schema):
date = fields.DateTime()
production = fields.Float()

class BatteryStatusSchema(Schema):
level = fields.Integer()
available = fields.Float()

class ChargeCommandSchema(Schema):
start_time = fields.DateTime()
energy = fields.Float()