# run.py

import os
from flask import Flask
from app import config
from app.api import api_blueprint
from app.models import prediction_model, storage_model

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['DEBUG'] = True

app.register_blueprint(api_blueprint)

@app.route('/')
def home():
return 'Welcome to the EnergyHub API!'

@app.route('/status')
def status():
return {'status': 'operational'}

if __name__ == '__main__':

prediction_model.load()
storage_model.load()

app.run(host='0.0.0.0', port=5000)