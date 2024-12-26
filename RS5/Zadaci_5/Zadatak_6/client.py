import asyncio, aiohttp
from aiohttp import web
import time

async def microservice_request(url, port): 
    async with aiohttp.ClientSession() as session:
        putanja = f"{url}:{port}/pozdrav"
        rezultat = await session.get(putanja)
        return await rezultat.json()


async def main():
    ##### sekvencijalno slanje zahtjeva
    start_time = time.time()
    odgovor1 = await microservice_request("http://localhost", 8081)
    odgovor2 = await microservice_request("http://localhost", 8082)
    end_time= time.time()

    print(odgovor1)
    print(odgovor2)
    print(f"Vrijeme izvršavanja (sekvencijalno slanje): {end_time - start_time:.2f} sek")

    ###### konkurentno slanje zahjeva
    start_time = time.time()
    odgovor1_task = asyncio.create_task(microservice_request("http://localhost", 8081))
    odgovor2_task = asyncio.create_task(microservice_request("http://localhost", 8082))
    odgovori = await asyncio.gather(odgovor1_task, odgovor2_task)
    end_time = time.time()
    
    print(odgovori[0])
    print(odgovori[1])
    print(f"Vrijeme izvršavanja (konkurentno slanje): {end_time - start_time:.2f} sek")


asyncio.run(main())