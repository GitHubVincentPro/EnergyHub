from flask import Flask

from .forecast import forecast_blueprint
from .storage import storage_blueprint

def create_app():
app = Flask(__name__)
app.register_blueprint(forecast_blueprint)
app.register_blueprint(storage_blueprint)
return app