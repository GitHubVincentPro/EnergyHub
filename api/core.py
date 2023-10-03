python
from .models import ForecastRequest, ForecastResult

def predict(request: ForecastRequest) -> ForecastResult:
# logique métier