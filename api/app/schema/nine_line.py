from pydantic import BaseModel

class NineLineBase(BaseModel):
    id: str
    audio_path: str
    audio_translation: str 

