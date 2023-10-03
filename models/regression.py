```python
from .linear_model import train_linear_model
from sklearn.tree import DecisionTreeRegressor

def train_decision_tree(X_train, y_train):
model = DecisionTreeRegressor()
model.fit(X_train, y_train)
return model
```