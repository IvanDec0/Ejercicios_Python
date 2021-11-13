# Ejercicio 6.13
def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

# Ejercicio 6.14
def donde_insertar(lista, x):
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if x == lista[medio]: # Caso de que el numero se encuentre en la lista
            return(f'\nEl número {x} se encuentra en la posición {medio}')
        if lista[medio] > x:
            der = medio -1
        else:
            izq = medio + 1
    return(f'\nEl número {x}, deberia ir en la posición {medio}')



# Ejercicio 6.15
def insertar(lista, x):
    lista_modificada = lista.copy()
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
    #print(busqueda_binaria([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],18, verbose = True)) # Descomentar para testear
    #print(donde_insertar([1,2,3,4,6,7,8,9], 5)) # Descomentar para testear
    #print(donde_insertar([-4,-3,-1], -2))
    print(insertar([3,4,5,6,7,8,9], 0)) # Descomentar para testear
    print(insertar([8,9,10,11,13,14], 12))
    print(insertar([-4,-3,-1], -2)) # Descomentar para testear

