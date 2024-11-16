tajni_broj = 55
broj_je_pogoden = False
brojac_pokusaja = 0

while broj_je_pogoden == False:
    broj = int(input("Unesi broj: "))
    brojac_pokusaja += 1

    if broj < 1 or broj > 100:
        print("Broj mora biti u rasponu od 1 do 100")
    elif broj < tajni_broj:
        print("Broj je veći.")
    elif broj > tajni_broj:
        print("Broj je manji.")
    elif broj == tajni_broj:
        print(f"Bravo, pogodio si u {brojac_pokusaja} pokusaja!")
        broj_je_pogoden = True
    
print("Igra gotova!")