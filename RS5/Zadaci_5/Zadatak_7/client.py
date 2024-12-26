import asyncio, aiohttp


async def microservice_zbroj(brojevi):
    async with aiohttp.ClientSession() as session:
        rezultat = await session.post("http://localhost:8083/zbroj", json=brojevi)
        return await rezultat.json()
    
async def microservice_umnozak(brojevi):
    async with aiohttp.ClientSession() as session:
        rezultat = await session.post("http://localhost:8084/umnozak", json=brojevi)
        return await rezultat.json()
    

async def microservice_kolicnik(zbroj, umnozak):
    async with aiohttp.ClientSession() as session:
        tijelo_zahtjeva = {"zbroj" : zbroj, "umnozak" : umnozak}
        rezultat = await session.post("http://localhost:8085/kolicnik", json=tijelo_zahtjeva)
        return await rezultat.json()



async def main():

    brojevi=[1,2,3,4,5]

    micro_zbroj_task1 = asyncio.create_task(microservice_zbroj({"brojevi":brojevi}))
    micro_umnozak_task2 = asyncio.create_task(microservice_umnozak({"brojevi":brojevi}))

    odgovor = await asyncio.gather(micro_zbroj_task1,micro_umnozak_task2)
    print(odgovor[0], odgovor[1])

    odgovor_kolicnik = await microservice_kolicnik(odgovor[0], odgovor[1])
    print("Količnik brojeva: ", odgovor_kolicnik["Kolicnik"])



asyncio.run(main())
