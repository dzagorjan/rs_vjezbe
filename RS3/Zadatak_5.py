import asyncio

podaci_kartice = [
    {'prezime': 'Marković', 'broj_kartice': '123456', 'CVV': '345'},
    {'prezime': 'Perić', 'broj_kartice': '567987', 'CVV': '786'},
    {'prezime': 'Ivić', 'broj_kartice': '987354', 'CVV': '997'}
]

async def secure_data(podaci):
    await asyncio.sleep(3)
    return {
        'prezime': podaci['prezime'], 
        'broj_kartice': hash(podaci['broj_kartice']),
        'CVV': hash(podaci['CVV'])
        }


async def main():
    zadaci = [asyncio.create_task(secure_data(podaci)) for podaci in podaci_kartice ]
    rezultat = await asyncio.gather(*zadaci)
    print(rezultat)


asyncio.run(main())