import asyncio
import time


async def dohvati_brojeve():
    start_time = time.time()

    print(f"Dohvaćam podatke..")
    lista_brojeva = [i for i in range(1,11)]
    await asyncio.sleep(3)
    print("Podaci dohvaćeni.")
    end_time = time.time()
    print(f"Vrijeme izvršavanja je: {end_time - start_time:.2f} sekundi.")
    return lista_brojeva

async def main():
    lista_brojeva = await dohvati_brojeve()
    print(f"Podaci: {lista_brojeva}")


asyncio.run(main())