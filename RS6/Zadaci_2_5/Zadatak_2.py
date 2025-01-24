from pydantic import BaseModel
from typing import Literal

class Admin(BaseModel):
    ime: str
    prezime: str
    korisnicko_ime: str
    email: str
    ovlasti: list[Literal["dodavanje", "brisanje", "ažuriranje", "čitanje"]] = []

