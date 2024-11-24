class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}, Cijena: {self.cijena}, Dostupna količina: {self.dostupna_kolicina}")

skladiste = [Proizvod("čokolada", 5, 103), Proizvod("mlijeko", 2, 355)]

def dodaj_proizvod(proizvod):
    skladiste.append(proizvod)
