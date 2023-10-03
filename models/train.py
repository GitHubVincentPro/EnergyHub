
```python
from .regression import train_linear_model, train_decision_tree

def run_training():
X_train, y_train = load_data()

linear_model = train_linear_model(X_train, y_train)
decision_tree = train_decision_tree(X_train, y_train)

return linear_model, decision_tree
```