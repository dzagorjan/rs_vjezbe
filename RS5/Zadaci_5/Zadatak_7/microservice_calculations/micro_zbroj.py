from aiohttp import web

app = web.Application()

async def post_zbroj(request):    
    tijelo_zahtjeva = await request.json()

    if (len(tijelo_zahtjeva['brojevi'])==0):
        return web.json_response({"message":"Nisu proslijeđeni podaci"}, status=400)

    brojevi = tijelo_zahtjeva.get("brojevi")
    zbroj = sum(brojevi)  
    print(f"Zbroj: {zbroj}")  
    
    return web.json_response({"zbroj": zbroj}, status=200)

app.router.add_post("/zbroj", post_zbroj)


web.run_app(app, host='localhost', port=8083)
