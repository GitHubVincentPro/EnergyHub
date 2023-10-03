class Config:
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True

# Dans app/__init__.py

from flask import Flask

def create_app():
app = Flask(__name__)
app.config.from_object('app.config.Config')

from app.api import api as api_blueprint
app.register_blueprint(api_blueprint)

from app.models import prediction, storage
return app