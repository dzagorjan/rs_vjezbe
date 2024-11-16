lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

def ukloni_duplikate(lista):
    skup_bezduplikata = set(lista)
    return list(skup_bezduplikata)

print(ukloni_duplikate(lista))
