from typing import List
from fastapi import FastAPI, HTTPException
from models import ObjavaResponse, ObjavaRequest
import datetime


app = FastAPI()

objave = [{"id": 1, "korisnik": "marko123", "tekst": "Danas je predivan dan!", "vrijeme": "2025-02-08T10:30:00Z"},
        {"id": 2, "korisnik": "ana_m", "tekst": "Upravo sam završila čitanje sjajne knjige!", "vrijeme": "2025-02-08T11:15:30Z"},
        {"id": 3, "korisnik": "petarP", "tekst": "Oduševljen sam novim filmom!", "vrijeme": "2025-02-08T12:05:20Z"},
        {"id": 4, "korisnik": "luka_99", "tekst": "Pogledajte moj novi crtež!", "vrijeme": "2025-02-08T13:40:10Z"},
        {"id": 5, "korisnik": "ivaS", "tekst": "Konačno završila projekt na kojem sam radila!", "vrijeme": "2025-02-08T14:25:50Z"}
    ]


@app.post("/objava", response_model=ObjavaResponse)
def dodaj_objavu(nova_objava:ObjavaRequest):
    new_id = len(objave)+1
    objava = ObjavaResponse(id=new_id,korisnik=nova_objava.korisnik, tekst=nova_objava.tekst, vrijeme=datetime.datetime.now())
    objave.append(objava)
    return objava



@app.get("/objava/{id}", response_model=ObjavaResponse)
def dohvati_objavu(id:int):
    for objava in objave:
        if objava["id"] == id:
            return objava
    raise HTTPException(status_code=404, detail="Nije pronađena tražena objava.")


@app.get("/korisnici/{korisnik}/objave", response_model=List[ObjavaResponse])
def dohvati_objavu_korisnik(korisnik:str):
    filtrirane_objave = [objava for objava in objave if objava["korisnik"] == korisnik]
    return filtrirane_objave