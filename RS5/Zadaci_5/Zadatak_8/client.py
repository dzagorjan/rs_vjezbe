import asyncio, aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        odgovor1 = await session.get("http://localhost:8086/cat/2")
        facts = await odgovor1.json()
        odgovor2 = await session.post("http://localhost:8087/facts", json=facts)
        facts_param = await odgovor2.json()
        print(facts_param)
    
asyncio.run(main())