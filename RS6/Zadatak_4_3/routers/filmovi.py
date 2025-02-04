from typing import List, Optional, Literal
from fastapi import APIRouter, HTTPException, Query
from models.film import ResponseFilm
import requests

filmoviRouter = APIRouter()

valid_filmovi = List[ResponseFilm]



def fetch_filmovi():
    response = requests.get("https://gist.githubusercontent.com/saniyusuf/406b843afdfb9c6a86e25753fe2761f4/raw/523c324c7fcc36efab8224f9ebb7556c09b69a14/Film.JSON")
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Greška prilikom dohvaćanja podataka.")
    global valid_filmovi
    data = response.json()
    valid_filmovi = [ResponseFilm(**film) for film in data]

fetch_filmovi()


def clean_year(year_str: str) -> str: #uklanjanje svega što je eventualno iza crtice, kako bi ostala godina
    cleaned_year = year_str.strip().split('-')[0]
    return cleaned_year if cleaned_year.isdigit() else "0" 


@filmoviRouter.get("/filmovi", response_model=List[ResponseFilm])
def get_all_filmovi(min_year: Optional[str] = Query(None), 
                max_year: Optional[str] = Query(None), 
                min_rating: Optional[float] = Query(0, ge=0, le=10),
                max_rating: Optional[float] = Query(0, ge=0, le=10),
                type: Optional[Literal['movie', 'series']] = Query(None)):


    result_filmovi = valid_filmovi

    if min_year:
        result_filmovi = [film for film in result_filmovi if clean_year(film.Year) >= min_year]

    if max_year:
        result_filmovi = [film for film in result_filmovi if clean_year(film.Year) <= max_year]

    if min_rating:
        result_filmovi = [film for film in result_filmovi 
                          if film.imdbRating is not None and film.imdbRating >= min_rating]

    if max_rating:
        result_filmovi = [film for film in result_filmovi 
                          if film.imdbRating is not None and film.imdbRating <= max_rating]

    if type:
        result_filmovi = [film for film in result_filmovi if film.Type == type] 


        return result_filmovi
    raise HTTPException(status_code=404, detail="Greška kod pronalaženja filmova")

@filmoviRouter.get("/film/{imdbID}", response_model=ResponseFilm)
def get_film_by_imdb(imdbID: str):
    for film in valid_filmovi:
        if film.imdbID == imdbID:
            return film
    raise HTTPException(status_code=404, detail="Film nije pronađen")


@filmoviRouter.get("/film/{title}", response_model=ResponseFilm)
def get_film_by_title(title:str):
    for film in valid_filmovi:
        if film.Title.lower == title.lower():
            return film
    raise HTTPException(status_code=404, detail="Film nije pronađen")
        

