import random
import timeit as tt
import numpy as np
import matplotlib.pyplot as plt

def merge_sort(lista, contador=0):
    """Ordena lista mediante el método merge sort.
        Pre: lista debe contener elementos comparables.
        Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
        contador+=1
    else:
        medio = len(lista) // 2
        contador+=1
        izq, contador = merge_sort(lista[:medio], contador)
        der, contador = merge_sort(lista[medio:], contador)
        lista_nueva, contador = merge(izq, der, contador)
    return lista_nueva, contador


def merge(lista1, lista2, contador):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
        Pre: lista1 y lista2 deben estar ordenadas.
        Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):
        contador += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado, contador

def ord_burbujeo(lista):
    contador = 0
    for j in range(1, len(lista)):
        for i in range(0, len(lista)-j):
            contador += 1
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return contador



def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
        Pre: Los elementos de la lista deben ser comparables.
        ost: la lista está ordenada."""
    contador = 0
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            contador += reubicar(lista, i + 1)
        else:
            contador += 1
    return contador

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
        dentro del segmento [0:p-1].
        Pre: p tiene que ser una posicion válida de lista."""
    v = lista[p]
    contador = 1 
    j = p
    lista[j] = lista[j - 1]
    j -= 1
    while j > 0:
        contador += 1
        if(v < lista[j - 1]):
            lista[j] = lista[j - 1]
            j -= 1
        else:
            break
    lista[j] = v
    return contador

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
        Pre: los elementos de la lista deben ser comparables.
        Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    contador = 0
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        pos, comp = buscar_max(lista, 0, n)
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[pos], lista[n] = lista[n], lista[pos]
        # reducir el segmento en 1
        n = n - 1
        contador += comp
    return contador

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
        lista de elementos comparables.
        La lista no debe ser vacía.
        a y b son las posiciones inicial y final del segmento"""
    pos_max = a
    contador = 0
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
        contador += 1
    return pos_max, contador

def generar_lista(N):
    lista = [random.randint(1, 1000) for i in range(N)]
    return lista

def generar_listas(Nmax):
    l = [generar_lista(e) for e,s in enumerate(range((Nmax)), start= 1)]
    return l

def experimento_timeit(Nmax):
    tiempos_seleccion = []
    tiempos_insercion = []
    tiempos_burbujeo = []
    tiempos_merge = []
    
    global lista
    listas = generar_listas(Nmax)
    
    for lista in listas:
        tiempos_seleccion.append(tt.timeit('ord_seleccion(lista.copy())', number = 1, globals = globals()))
        tiempos_insercion.append(tt.timeit('ord_insercion(lista.copy())', number = 1, globals = globals()))
        tiempos_burbujeo.append(tt.timeit('ord_burbujeo(lista.copy())', number = 1, globals = globals()))
        tiempos_merge.append(tt.timeit('merge_sort(lista.copy())', number = 1, globals = globals()))
        

    tiempos_seleccion = np.array(tiempos_seleccion)
    tiempos_insercion = np.array(tiempos_insercion)
    tiempos_burbujeo = np.array(tiempos_burbujeo)
    tiempos_merge = np.array(tiempos_merge)
    
    plt.figure()
    plt.title('Comparación de tiempos en métodos de ordenamiento')
    plt.xlabel('Largo de la lista')
    plt.ylabel('Tiempo')
    plt.plot(tiempos_merge, 'm:', label = 'Merge-Sort')     
    plt.plot(tiempos_burbujeo, 'r--', label = 'Burbujeo')     
    plt.plot(tiempos_insercion, 'b-', label = 'Inserción')
    plt.plot(tiempos_seleccion, 'g--', label = 'Selección')
    plt.legend()
    plt.tight_layout() 
    plt.show()
    
if __name__ == '__main__':
    experimento_timeit(100)