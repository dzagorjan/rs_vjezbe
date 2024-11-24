# 1. Kvadriranje broja:
kvadriraj = lambda x: x ** 2
print(kvadriraj(2))


# 2. Zbroji pa kvadriraj:
zbroji_pa_kvadriraj = lambda a, b : (a + b) ** 2
print(zbroji_pa_kvadriraj(2, 2))


# 3. Kvadriraj duljinu niza:
kvadriraj_duljinu_niza = lambda niz: len(niz) ** 2
print(kvadriraj_duljinu_niza("pocetak"))


# 4. Pomnoži vrijednost s 5 pa potenciraj na x:
pomnozi_i_potenciraj = lambda broj, x: (broj * 5) ** x
print(pomnozi_i_potenciraj(2, 2))


# 5. Vrati True ako je broj paran, inače vrati None:
paran_broj = lambda x: True if x % 2 == 0 else None
print(paran_broj(3))