from fastapi.routing import APIRouter
from typing import List
from app.crud.read import get_coas
from app.schema.coas import COABase

router = APIRouter()

@router.get('')
async def get_coas(id: str) -> List[COABase]:
    return get_coas(id)