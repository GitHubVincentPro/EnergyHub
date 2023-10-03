python
from .models import ForecastRequest, ForecastResult

def predict(request: ForecastRequest) -> ForecastResult:

# Logique métier de prédiction
result = make_prediction(request.location)

return ForecastResult(
temperature=result["temperature"],
weather=result["weather"]
)

def make_prediction(location):
# Appelle une API externe ou mock
return {"temperature": 15, "weather": "sunny"}