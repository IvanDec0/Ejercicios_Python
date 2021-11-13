# Valor de los fosforos: [0: Apagado, 1: Encendido, -1: Carbonizado(Quemado)]

def propagar(lista):
    j = 0 # Uso 'j' como contador, prodria utilizar enumerate
    # Recorro la lista de forma normal
    for i in lista:
        if lista[j] == 1:
            try:
                # Si el siguiente fosforo esta quemado saltea la iteracion
                if lista[j+1] == -1:
                    pass
                else:
                    # Si el fosforo siguiente no esta quemando, prendo el fosforo siguiente
                    try:
                        lista[j+1] = 1
                    except:
                        continue
            except:
                pass
        j = j +1
    # La variable 'j' le asigno el largo de la lista para iterar desde la ultima posicion
    j = len(lista) - 1
    # Recorro la lista de forma inversa
    for i in lista:
        if lista[j] == 1:
            try:
                # Si el siguiente fosforo esta quemado saltea la iteracion
                if lista[j-1] == -1:
                    pass
                else:
                    try:
                        # Si el fosforo siguiente no esta quemando, prendo el fosforo siguiente
                        lista[j-1] = 1
                    except:
                        continue
            except:
                pass
        j = j -1
    return lista

e = [0,0,0,0,0,0,1,0,0,0,0,0,0]
lista_1 = [ 0, 0, 0, 1, 0, 0]
lista_2 = [ 0, 0, 0, 0, 0, -1]
lista_3 = [ 0, 0, 0, 0, 0, 1]
lista_4 = []
lista_5 = [ 0 for _ in range(1000) ] + [1]
lista_6 = [1] + [ 0 for _ in range(1000) ]
lista_7 = [ (i% 6)//2-1 for i in range(200) ]
lista_8 = [ -1*((i% 6)//2-1) for i in range(60) ]
s = propagar(lista_8)
print(f'{s}')
            