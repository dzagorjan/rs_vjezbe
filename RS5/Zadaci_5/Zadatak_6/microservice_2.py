import asyncio, aiohttp
from aiohttp import web

app = web.Application()

async def handler_pozdrav2(request):
    await asyncio.sleep(4)
    return web.json_response({"message" : "Pozdrav nakon 4 sekunde"}, status=200)

app.router.add_get("/pozdrav", handler_pozdrav2)

web.run_app(app, host='localhost', port=8082)