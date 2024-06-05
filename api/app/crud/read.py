from .connect import es
from app.schema.nine_line import NineLineBase
from config import settings

def read_nine_line(id: str):
    result = es.search(settings.NINE_LINE_INDEX)
    return result