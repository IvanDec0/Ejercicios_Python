import random
import numpy as np
import matplotlib.pyplot as plt

def generar_lista(N):
    lista = [random.randint(1, 1000) for i in range(N)]
    return lista

def experimento_vectores(Nmax:int):
    lista_merge = []
    lista_burbuja = []
    lista_insercion = []
    lista_seleccion = []
    
    for i in range(1, Nmax+1, 1):
        lista = generar_lista(i)
        merge = merge_sort(lista.copy())
        merge = merge[1]
        burbujeo = ord_burbujeo(lista.copy())
        insercion  = ord_insercion(lista.copy())
        seleccion = ord_seleccion(lista.copy())
        #--------------------------------------
        lista_merge.append(merge)
        lista_burbuja.append(burbujeo)
        lista_insercion.append(insercion)
        lista_seleccion.append(seleccion)
        #---------------------------------------
    # Grafico
    plt.figure()
    plt.title('Comparación de métodos de ordenamiento')
    plt.xlabel('Largo de la lista')
    plt.ylabel('Cantidad de comparaciones')
    plt.plot(lista_merge, 'm:', label = 'Merge-Sort')     
    plt.plot(lista_burbuja, 'r--', label = 'Burbujeo')     
    plt.plot(lista_insercion, 'b-', label = 'Inserción')
    plt.plot(lista_seleccion, 'g*', label = 'Selección')
    plt.legend()
    plt.tight_layout() 
    plt.show()


def experimento(N:int, k:int):
    lista = []
    lista_merge = []
    lista_burbuja = []
    lista_insercion = []
    lista_seleccion = []
    for i in range(k):
        for j in range(N):
            num = random.randint(0, 1000)
            lista.append(num)
        #-------------------------------------
        simple_merge = merge_sort(lista)
        simple_burbuja = ord_burbujeo(lista)
        simple_insercion = ord_insercion(lista)
        simple_seleccion = ord_seleccion(lista)
        #--------------------------------------
        lista_merge.append(simple_merge)
        lista_burbuja.append(simple_burbuja)
        lista_insercion.append(simple_insercion)
        lista_seleccion.append(simple_seleccion)
        #---------------------------------------
    prom_merge = np.mean(lista_merge)
    prom_burbuja = np.mean(lista_burbuja)
    prom_insercion = np.mean(lista_insercion)
    prom_seleccion = np.mean(lista_seleccion)
    prom_merge = np.mean(prom_merge)
    #-------------------------------------------
    return (prom_merge, prom_burbuja, prom_insercion, prom_seleccion)

def merge_sort(lista:list, contador=0):
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


def merge(lista1:list, lista2:list, contador:int):
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

def ord_burbujeo(lista:list):
    contador = 0
    for j in range(1, len(lista)):
        for i in range(0, len(lista)-j):
            contador += 1
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return contador



def ord_insercion(lista:list):
    """Ordena una lista de elementos según el método de inserción.
        Pre: Los elementos de la lista deben ser comparables.
        Post: la lista está ordenada."""
    contador = 0
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            contador += reubicar(lista, i + 1)
        else:
            contador += 1
    return contador

def reubicar(lista:list, p):
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

def ord_seleccion(lista:list):
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

def buscar_max(lista:list, a, b):
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

if __name__ == '__main__':
    #print(experimento(10, 2))
    experimento_vectores(30)

