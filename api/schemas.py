python
from pydantic import BaseModel

class ForecastRequestSchema(BaseModel):
date: datetime
location: str

class ForecastResultSchema(BaseModel):
temp: float
weather: str