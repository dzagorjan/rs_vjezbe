broj_1 = float(input("Unesi broj 1: "))

broj_2 = float(input("Unesi broj 2: "))

operator = input("Unesi operator (+,-,*,/): ")

rezultat = float
dozvoljeni_operatori = ["+","-","*","/"]

if operator not in dozvoljeni_operatori:
    print("Nepodržani operator!")

if operator == "+":
    rezultat = broj_1 + broj_2
    print(f"Rezultat operacije {broj_1} {operator} {broj_2} je {rezultat}")

elif operator == "-":
    rezultat = broj_1 - broj_2
    print(f"Rezultat operacije {broj_1} {operator} {broj_2} je {rezultat}")

elif operator == "*":
    rezultat = broj_1 * broj_2
    print(f"Rezultat operacije {broj_1} {operator} {broj_2} je {rezultat}")

elif operator == "/":

    if broj_2 == 0:
        print("Dijeljenje s nulom nije dozvoljeno!")    

    rezultat = broj_1 / broj_2
    print(f"Rezultat operacije {broj_1} {operator} {broj_2} je {rezultat}")