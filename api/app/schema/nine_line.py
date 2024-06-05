from pydantic import BaseModel
from uuid import UUID

class NineLineBase(BaseModel):
    id: UUID
    audio_path: str
    audio_translation: str 

