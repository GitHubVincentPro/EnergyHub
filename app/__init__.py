from flask import Flask
from .config import get_config
from .api import forecast, storage

def create_app(app_env):

app = Flask(__name__)
app.config.from_object(get_config(app_env))

app.register_blueprint(forecast)
app.register_blueprint(storage)

return app