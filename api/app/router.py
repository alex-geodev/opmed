from fastapi import APIRouter

from app.endpoints import nine_line, coas

api_router = APIRouter()

api_router.include_router(nine_line.router, prefix='/nineline', tags=['nine_line'])
api_router.include_router(coas.router, prefix='/coa', tags=['coa'])

