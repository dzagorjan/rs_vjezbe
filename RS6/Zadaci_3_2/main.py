from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query, status
from models import CarResponse, CarWithPdv, BaseCar

app = FastAPI()

automobili = [
    {"id": 1, "marka": "Volvo", "model": "V40", "godina_proizvodnje": 2018, "cijena": 18000, "boja": "crna"},
    {"id": 2, "marka": "Volvo", "model": "XC60", "godina_proizvodnje": 2021, "cijena": 32000, "boja": "bijela"}
]

#Zadatak 1.

@app.get("/automobili/{id}", response_model=CarResponse)
def dohvati_automobil(id: int):
    for automobil in automobili:
        if automobil["id"] == id:
            return automobil
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Automobil nije pronađen")

#Zadatak 2.

@app.get("/automobili", response_model=List[CarResponse])
def dohvati_automobil(min_cijena: Optional[float] = Query(0.00, ge=0), 
                      max_cijena: Optional[float] = Query(0.00, ge=0),
                      min_godina: Optional[int] = Query(0, ge=1960),
                      max_godina: Optional[int] = Query(0, le=2025)):
    if min_cijena > max_cijena:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Minimalna cijena mora biti manja od maksimalne")
    if min_godina > max_godina:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Minimalna godina mora biti manja od maksimalne")


    filtrirani_automobili = []
    for automobil in automobili:
        if automobil["cijena"] >= min_cijena and automobil["cijena"] <= max_cijena and automobil["godina_proizvodnje"] >= min_godina and automobil["godina_proizvodnje"] <= max_godina:
            filtrirani_automobili.append(automobil)
            return filtrirani_automobili
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Automobil nije pronađen")

#Zadatak 3.

@app.post("/automobili", response_model=CarWithPdv)
def dodaj_automobil(automobil: BaseCar):
    for postojeci_automobil in automobili:
        if postojeci_automobil["marka"] == automobil.marka and postojeci_automobil["model"] == automobil.model and postojeci_automobil["godina_proizvodnje"] == automobil.godina_proizvodnje:
            raise HTTPException (status.HTTP_400_BAD_REQUEST, detail="Automobil već postoji.")
        new_id = len(automobili) + 1
        cijena_pdv = automobil.cijena*1.25
        novi_automobil: CarWithPdv = {"id": new_id, "cijena_pdv": cijena_pdv, **automobil.model_dump()}
        automobili.append(novi_automobil)
        return novi_automobil