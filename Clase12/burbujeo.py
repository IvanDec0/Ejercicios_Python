def ord_burbujeo(lista):
    num = len(lista)
    i = 0
    while i < num:
        j = i
        while j < num:
                if lista[i] > lista[j]:
                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux
                j = j + 1
        i = i + 1
    return lista


if __name__ == '__main__':
    lista_1 = [1, 2, -3, 8, 1, 5]
    print(ord_burbujeo(lista_1))

    lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
    print(ord_burbujeo(lista_3))