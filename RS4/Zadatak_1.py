import aiohttp
import asyncio
import time

async def fetch_users(session,i):
    print(f"Fetching user {i} ...")
    response = await session.get("https://jsonplaceholder.typicode.com/users")
    users_fetched = await response.json()
    return users_fetched

async def main():
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_users(session,i)) for i in range(1,6)]

        results = await asyncio.gather(*tasks)   

        name = [user["name"] for user in results[0]]
        email = [user["email"] for user in results[0]]
        username = [user["username"] for user in results[0]]

        print(f"Names: {name}")
        print(f"Emails: {email}")
        print(f"Usernames: {username}")

        end_time = time.time()
        print(f"Vrijeme izvršavanja: {end_time - start_time: .2f}")

asyncio.run(main())