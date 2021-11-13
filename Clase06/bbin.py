# Ejercicio 6.15
def insertar(lista, x):
    lista_modificada = lista.copy()
    if lista[len(lista)-1] < x:
        lista_modificada.append(x)
        return (f'\nLa lista modificada es {lista_modificada}, el número {x}, se agrego en la posición {len(lista)}')
    else:
        izq = 0
        der = len(lista) - 1
        while izq <= der:
            medio = (izq + der) // 2
            if x == lista[medio]:
                return(f'\nEl número {x} se encuentra en la posición {medio}')
            if lista[medio] > x:
                der = medio - 1
            else:
                izq = medio + 1
        lista_modificada.insert(medio, x)
        return(f'\nLa lista modificada es {lista_modificada}, el número {x}, se agrego en la posición {medio}')

if __name__ == '__main__':
    #print(insertar([3,4,5,6,7,8,9], 0)) # Descomentar para testear
    print(insertar([8,9,10,11,13,14], 18)) # Descomentar para testear
    #print(insertar([-4,-3,-1], -2)) # Descomentar para testear