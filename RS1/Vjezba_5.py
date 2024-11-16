# for petlja

broj = int(input("Unesi broj:"))

faktorijel=1

for i in range(1, broj+1):
    faktorijel = faktorijel*i
print(f"Faktorijel broja {broj} je {faktorijel}")



# while petlja

broj = int(input("Unesi broj:"))
brojac = 1
faktorijel = 1

while brojac <= broj:
    faktorijel *= brojac
    brojac +=1
print(f"Faktorijel broja {broj} je {faktorijel}")



# while petlja #2 - ne znam da li je ovo elegantno rjesenje jer se brojacu dodjeljuje vrijednost broj, a varijabli broj ostaje inicijalna vrijednost samo radi kasnijeg ispisa

broj = int(input("Unesi broj:"))
brojac = broj
faktorijel = 1

while brojac > 0:
    faktorijel *= brojac
    brojac -=1
print(f"Faktorijel broja {broj} je {faktorijel}")