import asyncio
from aiohttp import web
import hashlib



korisnici = [
  {"korisnicko_ime": "admin", "lozinka_hash" : "8d43d8eb44484414d61a18659b443fbfe52399510da4689d5352bd9631c6c51b"}, # lozinka = "lozinka123"
  {"korisnicko_ime": "markoMaric", "lozinka_hash" : "5493c883d2b943587ea09ab8244de7a0a88d331a1da9db8498d301ca315d74fa"}, # lozinka = "markoKralj123"
  {"korisnicko_ime": "ivanHorvat", "lozinka_hash" : "a31d1897eb84d8a6952f2c758cdc72e240e6d6d752b33f23d15fd9a53ae7c302"}, # lozinka = "lllllllllllozinka_123"
  {"korisnicko_ime": "Nada000", "lozinka_hash":"492f3f38d6b5d3ca859514e250e25ba65935bcdd9f4f40c124b773fe536fee7d"} # lozinka = "blablabla"
]

app = web.Application()

def hash_data(data:str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

async def add_korisnik(request):
    data = await request.json()

    korisnicko_ime = data.get("korisnicko_ime")
    lozinka = data.get("lozinka")

    if not korisnicko_ime or not lozinka:
        return web.json_response({"Greška" : "Fali korisničko ime ili lozinka."}, status=400)
    
    for korisnik in korisnici:
        if korisnik["korisnicko_ime"] == korisnicko_ime:
            return web.json_response({"Greška": "Korisnik već postoji."}, status=400)
        
    lozinka_hash = hash_data(lozinka)

    korisnik = {
        "korisnicko_ime" : korisnicko_ime,
        "lozinka_hash" : lozinka_hash
    }
    
    korisnici.append(korisnik)
    return web.json_response(korisnik)


async def login_korisnik(request):
    data = await request.json()
    korisnicko_ime = data.get("korisnicko_ime")
    lozinka = data.get("lozinka")

    if not korisnicko_ime or not lozinka:
        return web.json_response({"Greška": "Fali korisničko ime ili lozinka."})

    for korisnik in korisnici:
        if korisnik["korisnicko_ime"] == korisnicko_ime:
            if korisnik["lozinka_hash"] == hash_data(lozinka):
                return web.json_response({"Poruka" : "Korisnik uspješno prijavljen."}, status=200)
            return web.json_response({"Poruka": "Lozinka neispravna."},status=403)
    return web.json_response({"Poruka": "Korisnik ne postoji u bazi."},status=403)


app.router.add_routes([
    web.post('/register', add_korisnik),
    web.post('/login', login_korisnik)
])


web.run_app(app, host='0.0.0.0', port=9000)

