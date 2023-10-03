python
from fastapi import APIRouter

from .core import predict
from .schemas import ForecastRequestSchema

router = APIRouter()

@router.post('/forecast')
async def forecast(request: ForecastRequestSchema):
return predict(request)