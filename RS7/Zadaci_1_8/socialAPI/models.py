from datetime import datetime
from pydantic import BaseModel, Field

class ObjavaRequest(BaseModel):
    korisnik: str = Field(max_length=20)
    tekst: str = Field(max_length=280)
    vrijeme: datetime

class ObjavaResponse(ObjavaRequest):
    id: int
