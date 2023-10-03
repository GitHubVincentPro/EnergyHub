```python
import core

def test_forecast():
weather = ...
result = core.forecast_production(weather)
assert result[...]

def test_schedule():
forecast = [...]
schedule = core.schedule_storage(forecast)
assert schedule[...]
```