from aiohttp import web

app = web.Application()

async def post_facts(request):
    tijelo_zahtjeva = await request.json()
    odgovor = []

    for fact in tijelo_zahtjeva:
        if 'cat'.lower or 'cats'.lower in fact.lower():
            odgovor.append(fact)

    return web.json_response(odgovor, status=200)

app.router.add_post("/facts", post_facts)


web.run_app(app, host='localhost', port=8087)