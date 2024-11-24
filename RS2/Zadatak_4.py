
import math
from datetime import datetime

# 1. zadatak

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza
    
    def ispis(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Godina proizvodnje: {self.godina_proizvodnje}, Kilometraza: {self.kilometraza}")

    def starost(self):
        print(f"Starost automobila je: {int(datetime.now().year) - (int(self.godina_proizvodnje))} godina")


automobil = Automobil("Volvo", "V40", 2018, 132776)

automobil.ispis()
automobil.starost()


# 2. zadatak

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self):
        return self.a + self.b

    def oduzimanje(self):
        return self.a - self.b

    def mnozenje(self):
        return self.a * self.b

    def dijeljenje(self):
        return self.a / self.b

    def potenciranje(self):
        return self.a ** self.b

    def korijen(self):
        return math.sqrt(self.a)
    

# 3. zadatak

class Student:
    def __init__(self,ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objekti = [Student(student["ime"], student["prezime"], student["godine"], student["ocjene"]) for student in studenti]

najbolji_student = max(studenti_objekti, key = lambda student: student.prosjek())

print(najbolji_student.ime)


# 4. zadatak

class Krug:
    def  __init__(self, r):
        self.r = r

    def opseg(self):
        return 2 * self.r * math.pi
    
    def povrsina(self):
        return self.r**2 * math.pi
    
krug = Krug(12)

print(krug.opseg())
print(krug.povrsina())
    

# 5. zadatak

class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self. placa = placa

    def work(self):
        print(f"Radim na poziciji {self.pozicija}")


class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")
    
    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
            

radnik = Radnik ("Mirko", "prodavač", 1600)
manager = Manager("Franjo", "manager", 3500, "prodaja")

radnik.work()
manager.give_raise(radnik,200)
print(f"Ja sam radnik {radnik.ime}, radim na poziciji {radnik.pozicija}, i imam novu placu {radnik.placa}")





