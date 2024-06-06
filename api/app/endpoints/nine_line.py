from fastapi.routing import APIRouter
from typing import Optional
from fastapi import UploadFile
from app.crud.create import audio_2_nine_line, process_nine_line, write_to_db
from app.crud.read import get_nine_lines, get_nine_line

# from app.crud.delete import delete_salary
# from app.crud.create import create_salary
# from app.crud.search import search
# from app.schema.salary import SalaryBase

router = APIRouter()

@router.post('/create')
async def create(audio_file: UploadFile):
    nl = audio_2_nine_line(audio_file)
    proc_nl = process_nine_line(nl)
    write_to_db(proc_nl)
    return proc_nl

@router.get('')
async def get(id: Optional[str] = None):
    if id:
        nl_list = get_nine_line(id)
    else:
        nl_list = get_nine_lines()
    return nl_list