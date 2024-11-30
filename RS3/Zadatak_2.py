import asyncio
import time

async def dohvati_korisnika():
    print("Dohvaćanje podataka o korisnicima...")
    lista_korisnika = [ 
        {"ime":"Marko", "prezime": "Marić", "email": "markomaric77@yahoo.com"},
        {"ime":"Ivan", "prezime": "Ivić", "email": "ivanivic22@yahoo.com"},
        {"ime":"Pero", "prezime": "Perić", "email": "peroperic455@yahoo.com"} ]
    await asyncio.sleep(3)
    print("Podaci o korisnicima dohvaćeni!")
    return lista_korisnika


async def dohvati_proizvod():
    print("Dohvaćanje podataka od proizvodima...")
    lista_proizvoda = [
        {"naziv": "računalo", "vrsta": "elektronika"},
        {"naziv": "tipkovnica", "vrsta": "elektronika"},
        {"naziv": "miš", "vrsta": "elektronika"},
    ]
    await asyncio.sleep(5)
    print("Podaci o proizvodima dohvaćeni!")
    return lista_proizvoda


async def main():
    start_time = time.time()
    dohvat_korisnik, dohvat_proizvod = await asyncio.gather(dohvati_korisnika(),dohvati_proizvod())
    end_time = time.time()
    print(f"Korisnici: {dohvat_korisnik}")
    print(f"Proizvodi: {dohvat_proizvod}")
    print(f"Vrijeme izvršavanja dohvata: {end_time - start_time: .2f} sekundi.")

asyncio.run(main())