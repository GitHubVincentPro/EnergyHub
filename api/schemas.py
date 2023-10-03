python
from pydantic import BaseModel

class ForecastRequestSchema(BaseModel):
location: str
date: datetime

class ForecastResultSchema(BaseModel):
temperature: float
weather: str