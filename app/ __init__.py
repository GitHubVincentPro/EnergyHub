### __init__.py

importer Flask et initialiser l'application:

```python
from flask import Flask

app = Flask(__name__)

from . import routes
```