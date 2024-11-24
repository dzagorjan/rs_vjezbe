class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena
    
    def ispis_narudzbe(self):
        svi_proizvodi = [f"{proizvod["naziv"]} x {proizvod["kolicina"]}" for proizvod in self.naruceni_proizvodi]
        
        print(f"Naručeni proizvodi: {"', ".join(svi_proizvodi)}, Ukupna cijena: {self.ukupna_cijena} EUR")


narudzbe = []



def napravi_narudzbu(naruceni_proizvodi):
    if not isinstance(naruceni_proizvodi, list):
        return print("Argument mora biti lista")
    if len(naruceni_proizvodi) == 0:
        return print("Lista je prazna")
    
    for proizvod in naruceni_proizvodi:
        if not isinstance(naruceni_proizvodi,dict):
            return print("Svaki element mota biti rječnik")
        if not all(kljuc in proizvod for kljuc in ["naziv", "cijena", "dostupna_kolicina"]):
            return print("Rječnik mota sadržavati kljuceve naziv, cijena i količina")
        if (proizvod["dostupna_kolicina"] < 1):
            return print(f"Proizvod {proizvod.naziv} nije dostupan")
    
        ukupna_cijena += proizvod["cijena"] * proizvod["narucena_kolicina"]

    nova_narudzba = Narudzba(naruceni_proizvodi,ukupna_cijena)

    narudzbe.append(nova_narudzba)

    return nova_narudzba

