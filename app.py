```python
from ui import ui_bp

app = Flask(__name__)
app.register_blueprint(ui_bp)

if __name__ == '__main__':
app.run()
```