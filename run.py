# run.py

from app import create_app
from app.models import prediction_model, storage_model

app = create_app()

@app.before_first_request
def initialise_models():
prediction_model.load()
storage_model.load()

@app.route('/')
def home():
return 'Bienvenue sur l'API EnergyHub!'

@app.route('/status')
def status():
return {'status': 'en fonctionnement'}

if __name__ == '__main__':

port = int(os.environ.get('PORT', 5000))

app.run(host='0.0.0.0', port=port, debug=True)