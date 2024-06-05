from .connect import es
from app.schema.nine_line import NineLineBase
from config import settings

def update_nine_line(id: str, doc: dict):
    es.update(index=settings.NINE_LINE_INDEX, id=id, doc=doc)