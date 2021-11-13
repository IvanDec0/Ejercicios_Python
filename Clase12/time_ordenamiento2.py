#%% 
import random
import matplotlib.pyplot as plt
import sys
import timeit as tt



def generar_lista(N):
    lista = [random.randint(1, 1000) for i in range(N)]
    return(lista)



def ord_burbujeo(lista):
    for n in range(len(lista) - 1, 0, -1):
        for i in range(n):
            if lista[i] > lista[i + 1]:
                cambio = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = cambio
    return lista
    


def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        pos = buscar_max(lista, 0, n)
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[pos], lista[n] = lista[n], lista[pos]
        
        # reducir el segmento en 1
        n = n - 1
        
    return lista

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
        
    return pos_max




def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
                
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
                            
    return lista


def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
    
    v = lista[p]
        
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
        
    lista[j] = v
    


def merge_sort(lista, contador=0):
    """Ordena lista mediante el método merge sort.
        Pre: lista debe contener elementos comparables.
        Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)

    return lista_nueva


def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
        Pre: lista1 y lista2 deben estar ordenadas.
        Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado



def generar_listas(Nmax):
    lista = []
    for i in range(1, Nmax+1):
        lista.append(generar_lista(i))
        
    return(lista)
        


def experimento_timeit(Nmax):

    tiempo_burbujeo = []
    tiempo_insercion = []
    tiempo_seleccion = []
    tiempo_merge_sort = []
    
    listas = generar_listas(Nmax)
    
    global lista
    num = 10
    
    for lista in listas:
        tt_burbujeo = tt.timeit('ord_burbujeo(lista.copy())', number = num, globals = globals())
        tt_insercion = tt.timeit('ord_insercion(lista.copy())', number = num, globals = globals())
        tt_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = num, globals = globals())
        tt_merge_sort = tt.timeit('merge_sort(lista.copy())', number = num, globals = globals())
    
        tiempo_burbujeo.append(tt_burbujeo)
        tiempo_insercion.append(tt_insercion)
        tiempo_seleccion.append(tt_seleccion)
        tiempo_merge_sort.append(tt_merge_sort)
    
    return(tiempo_burbujeo, tiempo_insercion, tiempo_seleccion, tiempo_merge_sort)

def grafico(Nmax):
    lista = experimento_timeit(Nmax)
    plt.figure()
    plt.title('Comparación de métodos de ordenamiento mediante TimeIT')
    plt.xlabel('Largo de la lista')
    plt.xlim(0, Nmax+1)
    plt.ylabel('Cantidad de comparaciones')
    plt.plot(lista[0], label = 'burbujeo', color = 'red')
    plt.plot(lista[1], label = 'inserción', color = 'green' )
    plt.plot(lista[2], label = 'selección', color = 'blue')
    plt.plot(lista[3], label = 'merge', color = 'violet' )
    plt.legend()
    plt.tight_layout() 
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} numero de iteraciones')
    else:
        Nmax = int(sys.argv[1])
    grafico(Nmax)

# %%
