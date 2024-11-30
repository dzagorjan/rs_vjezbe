import asyncio


baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]


baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]


async def autentifikacija(korisnik, lozinka):

    print(f"Provjera korisnika {korisnik["korisnicko_ime"]}...") 
    await asyncio.sleep(3)
    for korisnik_u_bazi in baza_korisnika:        
        if korisnik["korisnicko_ime"] == korisnik_u_bazi["korisnicko_ime"] and korisnik["email"] == korisnik_u_bazi["email"]:   
            return await autorizacija(korisnik_u_bazi, lozinka) 
    else:
        return f"Korisnik {korisnik["korisnicko_ime"]} nije pronađen."
    


async def autorizacija(korisnik, lozinka):

    print("Autorizacija korisnika...")
    await asyncio.sleep(2)    
    for korisnik_lozinka in baza_lozinka:
        if korisnik["korisnicko_ime"] == korisnik_lozinka["korisnicko_ime"] and lozinka == korisnik_lozinka["lozinka"]:
            return f"Korisnik {korisnik["korisnicko_ime"]}: Autorizacija uspješna."
        else:
            return f"Korisnik {korisnik["korisnicko_ime"]}: autorizacija neuspješna."

async def main():

    korisnik = {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com', 'lozinka': 'lozinka123'}
    rezultat = await autentifikacija(korisnik, korisnik["lozinka"])
    print(rezultat)

asyncio.run(main())

