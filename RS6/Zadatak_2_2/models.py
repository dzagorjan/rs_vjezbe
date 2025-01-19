from pydantic import BaseModel

class ResponseFilm(BaseModel):
    id: int
    naziv: str
    genre: str
    godina: int


class CreateFilm(BaseModel):
    naziv: str
    genre: str
    godina: int
    
