import asyncio, aiohttp
from aiohttp import web 

app = web.Application()

async def handler_pozdrav1(request):
    await asyncio.sleep(3)
    return web.json_response({"message" : "Pozdrav nakon 3 sekunde"}, status=200)

app.router.add_get("/pozdrav", handler_pozdrav1)

web.run_app(app, host='localhost', port=8081)