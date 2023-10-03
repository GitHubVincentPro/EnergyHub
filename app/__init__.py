from app.config import get_config

config = get_config(os.environ.get('FLASK_ENV'))

app = Flask(__name__)
app.config.from_object(config)