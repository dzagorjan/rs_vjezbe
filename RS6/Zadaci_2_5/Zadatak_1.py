from pydantic import BaseModel
from datetime import datetime

class Knjiga(BaseModel):
    naslov: str
    ime_autora: str
    prezime_autora: str
    godina_izdavanja: int = datetime.now().year
    broj_stranica: int
    izdavac: str

class Izdavac(BaseModel):
    naziv: str
    adresa: str