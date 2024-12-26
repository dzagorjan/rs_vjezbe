import asyncio, aiohttp
from aiohttp import web

app = web.Application()

async def handler_kolicnik(request):
    tijelo_zahtjeva = await request.json()
    
    zbroj = tijelo_zahtjeva.get('zbroj')
    umnozak = tijelo_zahtjeva.get('umnozak')
    print(zbroj)
    print(umnozak)

    if zbroj["zbroj"] == 0:
        return web.json_response({"message":"Ne može se dijeliti s nulom"}, status=400)

    kolicnik = umnozak["umnozak"]/zbroj["zbroj"]
    print(f"Količnik: {kolicnik}")  

    return web.json_response({"Kolicnik" : kolicnik})


app.router.add_post("/kolicnik", handler_kolicnik)

web.run_app(app, host='localhost', port=8085)