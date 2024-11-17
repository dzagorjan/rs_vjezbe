lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def grupiranje_po_paritetu(lista):

    parni = []
    neparni = []

    for i in lista:
        if i % 2 == 0:
            parni.append(i)
        else:
            neparni.append(i)
    return {"Parni": parni, "Neparni": neparni}


print(grupiranje_po_paritetu(lista))
