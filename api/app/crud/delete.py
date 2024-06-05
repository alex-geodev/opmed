from .connect import es
from config import settings
from uuid import UUID

def delete_nine_line(id: UUID):
    es.delete(index=settings.NINE_LINE_INDEX,id=id)