from aiohttp import web
import aiohttp, asyncio

app = web.Application()


proizvodi = [
  {"id": 1, "naziv": "Laptop", "cijena": 5000},
  {"id": 2, "naziv": "Miš", "cijena": 100},
  {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
  {"id": 4, "naziv": "Monitor", "cijena": 1000},
  {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

narudzbe = []

async def get_proizvodi(request):
    return web.json_response(proizvodi, status=200)

async def get_proizvod(request):
    id = request.match_info["id"]
    for proizvod in proizvodi:
        if proizvod["id"] == int(id):
            return web.json_response(proizvod)
    return web.json_response({"error": f"Proizvod s trazenim ID-em {id} ne postoji"}, status=404)


async def post_narudzbe(request):
    data = await request.json()
    proizvod_id = data.get("proizvod_id")
    kolicina = data.get("kolicina")

    proizvod = [proizvod for proizvod in proizvodi if proizvod['id'] == proizvod_id]
    if not proizvod:
        return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)
    
    narudzba = {
        "proizvod_id" : proizvod_id,
        "kolicina" : kolicina
    }
    
    narudzbe.append(narudzba)
    return web.json_response(narudzbe, status=201)
    


app.router.add_get("/proizvodi", get_proizvodi)
app.router.add_get("/proizvodi/{id}", get_proizvod)
app.router.add_post("/narudzbe", post_narudzbe)

async def pokreni_posluzitelj():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8081)
    await site.start()
    print("Posluzitelj pokrenut")


async def main():
    await pokreni_posluzitelj()

    async with aiohttp.ClientSession() as session:
        print("Klijentska sesija otvorena.")
    
        #GET proizvodi
        odgovor_proizvodi = await session.get("http://localhost:8081/proizvodi")
        odgovor_proizvodi_list = await odgovor_proizvodi.json() 
        print("Odgovor proizvodi", odgovor_proizvodi_list)

        #GET proizvod - postojeći ID
        odgovor_proizvod = await session.get("http://localhost:8081/proizvodi/1")
        odgovor_proizvod_list = await odgovor_proizvod.json()
        print("Odgovor proizvod", odgovor_proizvod_list)
        
        #GET proizvod - nepostojeći ID
        odgovor_proizvod = await session.get("http://localhost:8081/proizvodi/6")
        odgovor_proizvod_list = await odgovor_proizvod.json()
        print("Odgovor proizvod", odgovor_proizvod_list)

        #POST narudžba
        data = {"proizvod_id": 2, "kolicina": 5 }
        post_naruzdba = await session.post("http://localhost:8081/narudzbe", json=data)
        post_narudzba_list = await post_naruzdba.json()
        print("Odgovor narudžba", post_narudzba_list)

        #POST narudžba - invalid
        data_invalid = {"proizvod_id": 9, "kolicina": 5 }
        post_naruzdba = await session.post("http://localhost:8081/narudzbe", json=data_invalid)
        post_narudzba_list = await post_naruzdba.json()
        print("Odgovor narudžba", post_narudzba_list)


asyncio.run(main())