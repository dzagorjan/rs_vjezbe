from shop import proizvodi
from shop import narudzbe

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

[proizvodi.dodaj_proizvod(proizvodi.Proizvod(proizvod["naziv"], proizvod["cijena"], proizvod["dostupna_kolicina"])) for proizvod in proizvodi_za_dodavanje]


for proizvod in proizvodi.skladiste:
    proizvod.ispis()

narudzbe.narudzbe.append(narudzbe.napravi_narudzbu(proizvodi_za_dodavanje))






