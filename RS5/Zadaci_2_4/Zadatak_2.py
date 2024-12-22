from aiohttp import web

app = web.Application()

proizvodi = [
    {"naziv": "PC", "cijena": 3000, "kolicina": 2},
    {"naziv": "Tipkovnica", "cijena": 150, "kolicina": 10},
    {"naziv":"Miš", "cijena":50, "kolicina":10}
]
async def get_proizvodi(request):
    return web.json_response(proizvodi)

async def post_proizvodi(request):
    proizvod = await request.json()
    proizvodi.append(proizvod)
    print("Dodan proizvod..", proizvod)
    print("Nova lista proizvoda: ", proizvodi)
    
    return web.json_response(proizvodi, status=200)

app.router.add_get("/proizvodi", get_proizvodi)
app.router.add_post("/proizvodi", post_proizvodi)

web.run_app(app, host='localhost', port=8081)