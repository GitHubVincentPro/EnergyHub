python
from fastapi import APIRouter
from .schemas import *
from .core import predict

router = APIRouter()

@router.post('/forecast')
async def forecast():
# gestion de la route