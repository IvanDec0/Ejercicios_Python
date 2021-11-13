#%%
# Ejercicio 4.3
def buscar_u_elemento(lista, e):
    posicion = -1
    for i, z in enumerate(lista):
        if z == e:
            posicion = i
    return posicion

print(buscar_u_elemento((1,2,3,4,5,1,2,3,1,1,2), 5))

def buscar_n_elemento(lista, e):
    cantidad = 0
    for i, z in enumerate(lista):
        if z == e:
            cantidad = cantidad + 1 
    return cantidad

print(buscar_n_elemento((1,2,3,4,5,1,2,3,1,1,2), 2))
# %%
# Ejercicio 4.4
def maximo(lista):
    m = lista[0] # Lo inicializo en la primer variable de la lista para que funcione con numeros negativos
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m

print(maximo((-3,-2,-10)))


def minimo(lista):
    m = lista[0] # Lo inicializo en la primer variable de la lista
    for e in lista: # Recorro la lista y voy guardando el menor
        if e < m:
            m = e
    return m

print(minimo((-3,-2,-10)))
# %%
