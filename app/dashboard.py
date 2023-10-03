```python
from flask import render_template
from ui import layout

@app.route('/')
def home():
return render_template('index.html', layout=layout)
```