```python
from flask import Blueprint, render_template

ui_bp = Blueprint('ui', __name__)

@ui_bp.route('/')
def home():
return render_template('index.html')

@ui_bp.route('/forecast')
def forecast():
forecasts = get_predictions()
return render_template('forecast.html', forecasts=forecasts)

```