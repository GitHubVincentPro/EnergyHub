from flask import jsonify

class BadRequest(Exception):
status_code = 400

def __init__(self, message):
self.message = message