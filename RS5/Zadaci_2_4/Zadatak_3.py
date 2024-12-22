from aiohttp import web

app = web.Application()

korisnici = [
  {'ime': 'Ivo', 'godine': 25},
  {'ime': 'Ana', 'godine': 17},
  {'ime': 'Marko', 'godine': 19},
  {'ime': 'Maja', 'godine': 16},
  {'ime': 'Iva', 'godine': 22}
]

novi_korisnici=[]

async def get_punoljetni(request):
    novi_korisnici = [korisnik for korisnik in korisnici if korisnik['godine']>=18]
    return web.json_response(novi_korisnici, status=200)


app.router.add_get("/punoljetni", get_punoljetni)


web.run_app(app, host='localhost', port=8082)