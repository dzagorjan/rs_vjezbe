import aiohttp
import asyncio


async def get_dog_fact(session):
    response = await session.get("https://dogapi.dog/api/v2/facts")
    dog_fact = await response.json()
    return dog_fact['data'][0]['attributes']['body']

async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    cat_fact = await response.json()
    return cat_fact['fact']

async def mix_facts(dog_facts, cat_facts):
    return[dog_fact if len(dog_fact) > len(cat_fact) else cat_fact for dog_fact, cat_fact in zip(dog_facts,cat_facts)]


async def main():
    async with aiohttp.ClientSession() as session:
        task_dog_facts = [asyncio.create_task(get_dog_fact(session)) for _ in range (5)]
        task_cat_facts = [asyncio.create_task(get_cat_fact(session)) for _ in range (5)]
        dog_cat_facts = await asyncio.gather(*task_dog_facts, *task_cat_facts)

        dog_facts = dog_cat_facts[:5]
        cat_facts = dog_cat_facts[5:]

        mixed_facts = await mix_facts(dog_facts, cat_facts)

        print("Mixane činjenice o psima i mačkama:")
        for fact in mixed_facts:
            print(fact)

asyncio.run(main())