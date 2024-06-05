from re import M
from fastapi.routing import APIRouter

from fastapi import UploadFile
from app.crud.create import audio_2_nine_line

# from app.crud.delete import delete_salary
# from app.crud.create import create_salary
# from app.crud.search import search
# from app.schema.salary import SalaryBase

router = APIRouter()

@router.post('/create')
async def create(audio_file: UploadFile):
    nl = audio_2_nine_line(audio_file)
    return nl