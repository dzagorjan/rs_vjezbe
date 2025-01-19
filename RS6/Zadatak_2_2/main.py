from fastapi import FastAPI

from models import ResponseFilm,CreateFilm


app = FastAPI()

filmovi = [
  {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
  {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
  {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
  {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]

validirani_filmovi = [ResponseFilm(**film) for film in filmovi]

#Zadatak 1, 2, 5

@app.get("/filmovi", response_model=list[ResponseFilm])
def get_filmovi(genre: str = None, min_godina: int = 2000):
    #print(type(ResponseFilm))
    rezultat = [film for film in validirani_filmovi if film.genre == genre or film.godina == min_godina]
    # print(type(validirani_filmovi))
    # return validirani_filmovi
    return rezultat    


    



#Zadatak 3

@app.get("/filmovi/{id}", response_model=ResponseFilm)
def get_film_by_id(id: int):
    for validirani_film in validirani_filmovi:
        if validirani_film.id == id:
            #print(type(validirani_film))
            return validirani_film
        

#Zadatak 4

@app.post("/filmovi", response_model=ResponseFilm)
def add_film(film: CreateFilm):
    new_id = len(filmovi) + 1
    film_s_id = ResponseFilm = {"id": new_id, **film.model_dump()}
    validirani_filmovi.append(film_s_id)
    return film_s_id