import asyncio, aiohttp
from aiohttp import web

app = web.Application()


async def get_cat_fact():
    async with aiohttp.ClientSession() as session:
        response = await session.get("https://catfact.ninja/fact")
        cat_fact = await response.json()
    return cat_fact['fact']

async def get_cat(request):
    amount = int(request.match_info['amount'])
    tasks = []
    for i in range(0,amount):
        tasks.append(asyncio.create_task(get_cat_fact()))
    cat_facts = await asyncio.gather(*tasks)

    return web.json_response(cat_facts, status=200)

app.router.add_get("/cat/{amount}", get_cat)


web.run_app(app, host='localhost', port=8086)