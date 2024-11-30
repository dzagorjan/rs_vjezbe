import asyncio
import random

async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    if broj % 2 == 0:
        return f"Broj {broj} je paran."
    else:
        return f"Broj {broj} je neparan."
    

async def main():
    lista_brojeva = [random.randint(1,100) for _ in range(10)]    
    print (f"Lista brojeva: {lista_brojeva}")
    zadaci = [asyncio.create_task(provjeri_parnost(lista_brojeva[i])) for i in range(len(lista_brojeva))]
    rezultat = await asyncio.gather(*zadaci)
    print(rezultat)

asyncio.run(main())