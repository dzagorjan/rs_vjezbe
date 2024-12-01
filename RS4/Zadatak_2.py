import aiohttp
import asyncio
import time

async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    cat_facts = await response.json()
    return cat_facts

async def filter_cat_facts(list_cat_facts):
    final_cat_facts = [fact['fact'] for fact in list_cat_facts if 'cat' in fact['fact'].lower() or 'cats' in fact['fact'].lower()]
    return final_cat_facts


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_cat_fact(session)) for _ in range(20)]
        results = await asyncio.gather(*tasks)

    print("Filtrirane činjenice o mačkama:")
    for fact in await filter_cat_facts(results):
        print(f"- {fact}")

asyncio.run(main())
