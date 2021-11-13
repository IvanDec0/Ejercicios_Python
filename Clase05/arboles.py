#%%
# Ejercicio 5.25

import csv
import matplotlib.pyplot as plt

def leer_arboles(nombre_archivo):
    especie = 'Jacarandá'
    with open(nombre_archivo,'rt', encoding='utf-8', ) as af:
        registros=csv.reader(af)
        encabezados =next(registros)
        arboleda=[]
        for fila in registros:
            arboleda+=[dict(zip(encabezados,fila))]
            if especie == fila[7]:
                H=[float(arbol[3]) for arbol in registros] # Si utilizo (arbol['altura_tot']) no funciona

        return H

arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
plt.hist(arboleda,bins=55)
plt.show()

#%%
# Ejercicio 5.26
import csv
import matplotlib.pyplot as plt
import numpy as np

def leer_arboles(nombre_archivo):
    especie = 'Jacarandá'
    with open(nombre_archivo,'rt', encoding='utf-8', ) as af:
        registros=csv.reader(af)
        encabezados =next(registros)
        arboleda=[]
        H=[]
        for fila in registros:
            arboleda+=[dict(zip(encabezados,fila))]
            if especie == fila[7]: 
                #H=[(float(arbol[3]), float(arbol[4])) for arbol in registros] # Si utilizo (arbol['altura_tot']) y (arbol['diametro']) no funciona
                H.append((float(fila[3]), float(fila[4])))
    return H


def scatter_hd(lista_de_pares):
    # Creo una lista con colores
    colores= ['c','m','deeppink','aqua','lawngreen','r','fuchsia']
    # Elijo un elemento random de la lista de colores y la guardo en 'c'
    c = np.random.choice(colores)
    # Transformo la lista en un array de numpy
    listaNumpy=np.asarray(lista_de_pares)
    # Separo el array en 2 arrays diferentes
    h, d = np.split(listaNumpy, 2, axis=1)
    # Muestro el grafico
    plt.scatter(d,h,color=c, alpha=0.3)
    plt.xlabel("Diametro (cm)")
    plt.ylabel("Alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")


if __name__ == '__main__':
    arbol= leer_arboles('../Data/arbolado-en-espacios-verdes.csv')    
    scatter_hd(arbol)


# %%
