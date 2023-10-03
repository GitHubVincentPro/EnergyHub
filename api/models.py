python
from pydantic import BaseModel

class ForecastRequest(BaseModel):
location: str
date: datetime

class ForecastResult(BaseModel):
temperature: float
weather: str