from typing import TypedDict
from pydantic import BaseModel

class Jelo(BaseModel):
   identifikator: str
   naziv: str
   cijena: float

class Stol_Info(TypedDict):
   broj: int
   lokacija: str

class Narudzba(BaseModel):
   indentifikator: int
   ime_kupca: str
   stol_info: Stol_Info
   lista_jela: Jelo
   ukupna_cijena: float 

class RestaurantOrder(Narudzba):
   pass 