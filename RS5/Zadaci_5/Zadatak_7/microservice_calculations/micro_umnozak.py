from aiohttp import web

app = web.Application()

async def post_umnozak(request):
    tijelo_zahtjeva = await request.json()

    if (len(tijelo_zahtjeva['brojevi'])==0):
        return web.json_response({"message":"Nisu proslijeđeni podaci"}, status=400)


    brojevi = tijelo_zahtjeva.get("brojevi")
    
    umnozak=1

    for broj in brojevi:
        umnozak *= broj
    print(f"Umnožak: {umnozak}")
        
    return web.json_response({"umnozak" : umnozak}, status=200)

app.router.add_post("/umnozak", post_umnozak)


web.run_app(app, host='localhost', port=8084)