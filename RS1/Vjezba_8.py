lista_orig = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_parni = []

def filtriraj_parne(lista):
    for i in lista:
        if i % 2 == 0:
            lista_parni.append(i)
    print(lista_parni)

filtriraj_parne(lista_orig)