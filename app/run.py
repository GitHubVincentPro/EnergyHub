# app/run.py

from flask import Flask
from app import api

app = Flask(__name__)
app.register_blueprint(api.api)

@app.route('/')
def home():
return "Bienvenue sur l'API EnergyHub!"

@app.route('/status')
def status():
return "Tout fonctionne correctement"