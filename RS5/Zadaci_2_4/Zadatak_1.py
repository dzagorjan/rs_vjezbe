from aiohttp import web

app = web.Application()

proizvodi=[
    {"naziv":"PC", "cijena":3000, "kolicina":2},
    {"naziv":"Tipkovnica", "cijena":150, "kolicina":10},
    {"naziv":"Miš", "cijena":50, "kolicina":10}
]

async def get_proizvodi(request):
    return web.json_response(proizvodi)

app.router.add_get("/proizvodi", get_proizvodi)


web.run_app(app, host='localhost', port=8081)



