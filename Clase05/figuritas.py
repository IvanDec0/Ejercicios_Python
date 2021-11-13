#%%
# Ejercicios con figuritas sueltas
import numpy as np
import random
# Ejercicio 5.10
def crear_album(figus_total):
    A = []
    # Creo un array con valores en 0
    A = np.zeros(figus_total, dtype=np.int64)
    return A


# Ejercicio 5.11
def album_incompleto(A):
    return 0 in A


# Ejercicio 5.12
def comprar_figu(figus_total):
    # Creo un numero aleatorio correspondiente con el numero de figurita
    return random.randint(0,figus_total)

# Ejercicio 5.13
def cuantas_figus(figus_total):
    compradas = 0
    # Creo un album con todos valores 0
    album_lleno = crear_album(figus_total)
    # Itero el album en busqueda de si por lo menos falta una figurita
    while album_incompleto(album_lleno) == True: 
        # Llamo a la funcion que genera un numero random de figurita
        c = comprar_figu(figus_total)
        compradas = compradas + 1
        # Recorro el album y busco la posicion de la figurita que me acaba de generar de forma aleatoria,
        # y incremento en 1 esa posicion del album
        for k,_ in enumerate(album_lleno):
                if k == c:
                    album_lleno[k]+=1
    #return album_lleno,compradas
    return compradas

# Ejercicio 5.14
    # Lleno albumnes n cantidad de veces, con 6 figuritas cada album
def experimento_figus514(n_repeticiones):
    lista = []
    figus_total = 6
    # Itero n veces, comprando figuritas y llenando el album
    for _ in range(n_repeticiones):
        f = cuantas_figus(figus_total) # Aca se me complico con la comprensión de listas, por lo cual lo hice asi
        lista.append(f)
    #print(lista)
    # Obtengo el promedio de figuritas 'compradas' en cada album
    promedio = np.mean(lista)
    return int(promedio)

# Ejercicio 5.15
# Lleno albumnes n cantidad de veces, con x figuritas cada album
def experimento_figus(n_repeticiones, figus_total):
    lista = []
    # Itero n veces, comprando figuritas y llenando el album
    for _ in range(n_repeticiones):
        f = cuantas_figus(figus_total)
        lista.append(f)
    #print(lista)
    # Obtengo el promedio de figuritas 'compradas' en cada album
    promedio = np.mean(lista)
    return int(promedio)

if __name__ == '__main__':
    #print(cuantas_figus(670)) # Descomentar esta linea para probar la función
    #print(experimento_figus514(1000)) # Descomentar esta linea para probar la función
    print(experimento_figus(5, 670)) # Descomentar esta linea para probar la función

#%%
# Ejercicios con paquetes de figuritas
import numpy as np
import random
import matplotlib.pyplot as plt

def crear_album(figus_total):
    A = []
    # Creo un array con valores en 0
    A = np.zeros(figus_total, dtype=np.int64)
    return A

def album_incompleto(A):
    return 0 in A

# Ejercicio 5.16
def comprar_figu_paquete(figus_total):
    paquete=[]
    # Creo 5 numeros aleatorios correspondiente con el numero de figurita y lo guardo en un paquete
    for i in range(5):
        paquete.append(random.randint(0,figus_total))
    return paquete

# Ejercicio 5.17
def comprar_paquete(figus_total, figus_paquete):
    paquete=[]
    # Creo n numeros aleatorios correspondiente con el numero de figurita y lo guardo en un paquete
    for i in range(figus_paquete):
        paquete.append(random.randint(0,figus_total))
    return paquete

# Ejercicio 5.18
def cuantos_paquetes(figus_total, figus_paquete):
    compradas = 0
    # Creo un album con todos valores 0
    album_lleno = crear_album(figus_total)
    # Itero el album en busqueda de si por lo menos falta una figurita
    while album_incompleto(album_lleno) == True: 
        # Llamo a la funcion que genera un numero random de figurita
        c = comprar_paquete(figus_total, figus_paquete)
        compradas = compradas + 1
        # Recorro el album y busco la posicion de la figurita que me acaba de generar de forma aleatoria,
        # y incremento en 1 esa posicion del album
        for k,_ in enumerate(album_lleno):
            for j,i in enumerate(c):
                if k == i:
                    album_lleno[k]+=1
    #return album_lleno,compradas
    return compradas


# Ejercicio 5.19
def promedio_paquete(n_repeticiones, figus_total, figus_paquete):
    compras = []
    for i in range(n_repeticiones+1):
        f = cuantos_paquetes(figus_total, figus_paquete)
        compras.append(f)
    promedio = np.mean(compras)
    return int(promedio)


# Ejercicio 5.20
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    i = 1
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        for k,_ in enumerate(album):
            for j,i in enumerate(paquete):
                if k == i:
                    album[k]+=1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas


def grafica_figus_pegadas(figus_total, figus_paquete):
    plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
    plt.xlabel("Cantidad de paquetes comprados.")
    plt.ylabel("Cantidad de figuritas pegadas.")
    plt.title("La curva de llenado se desacelera al final")
    plt.show()


# Ejercicio 5.20 parte 2
def probabilidad_850_paquetes(n_repeticiones, figus_total, figus_paquete):
    compras = []
    for _ in range(n_repeticiones+1):
        f = cuantos_paquetes(figus_total, figus_paquete)
        compras.append(f)
    n_paquetes_hasta_llenar=np.array(compras)
    probabilidad = (n_paquetes_hasta_llenar <= 850).sum()
    return int(probabilidad)


# Ejercicio 5.21
def plotear_figus(n_repeticiones, figus_total, figus_paquete):
    lista = []
    for _ in range(n_repeticiones+1):
        figuritas = cuantos_paquetes(figus_total, figus_paquete)
        lista.append(figuritas)
    plt.hist(lista,bins=180)
    plt.xlabel("Cantidad de paquetes comprados.")
    plt.ylabel("Albumes.")
    plt.title("Cantidad de figuritas compradas en cada album")
    plt.show()


if __name__ == '__main__':
    #print(cuantos_paquetes(50, 6)) # Descomentar esta linea para probar la función
    print(promedio_paquete(50,6,5)) # Descomentar esta linea para probar la funcion
    #grafica_figus_pegadas(670,5) # Descomentar esta linea para probar la función
    #print(probabilidad_850_paquetes(50,670,5)) # Descomentar esta linea para probar la función
    #plotear_figus(100,670,5) # Descomentar esta linea para probar la función

# %%
