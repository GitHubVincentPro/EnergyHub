```python
import dash
import dash_html

app = dash.Dash()

app.layout = html.Div([

# Widget de prévision
html.H1("Production prévue"),

# Graphique de planification
dcc.Graph(id='schedule-graph'),

# Boutons de commande
html.Button("Démarrer"),

])

@app.callback(...)
def update_graph():
...
```