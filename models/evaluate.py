```python
from . import train

def evaluate_models():
models = train.run_training()

for model in models:
score = evaluate(model, X_test, y_test)
print(score)
```