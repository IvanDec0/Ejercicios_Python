import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint(-1,2,largo) 
    return pasos.cumsum()

def graficar():
    N = 100000
    lista = []
    mas_alejada = []
    menos_alejada = []
    for _ in range(12):
        caminata = (randomwalk(N))  # Genero una lista de caminatas
        lista.append(caminata)
        
    for nro, _ in enumerate(lista):
        if nro == 0: # Si es la primera iteacion guardo el maximo de la primera caminata
            lejos = max(abs(lista[nro]))
            cerca = max(abs(lista[nro]))
            maxima = nro
            minima = nro
        if lejos < max(abs(lista[nro])): # Busco la caminata con el maximo mas grande
            lejos = max(abs(lista[nro]))
            maxima = nro
        if cerca > max(abs(lista[nro])): # Busco la caminata con el maximo mas chico
            cerca = max(abs(lista[nro]))
            minima = nro
    mas_alejada.append(lista[maxima]) # Creo una lista con la caminata con el maximo mas grande
    menos_alejada.append(lista[minima]) # Creo una lista con la caminata con el maximo mas chico

    # Comienzo a plotear
    fig = plt.figure()
    for i, caminata in enumerate(lista):
        plt.subplot(2, 1, 1) # define la figura de arriba
        plt.title("12 Caminatas al azar", color='blue', fontname='Italic', fontsize=18)
        plt.xlabel("Tiempo.", fontsize=9, color='c')
        plt.ylabel("Distancia al Origen.", color='c')
        plt.ylim(-1000, 1000)
        ticks = [-1000, -500, 0, 500, 1000] # Seteo la escala de los valores de los ejes
        plt.yticks(ticks=ticks, fontsize=10, color='k') # Seteo la escala de los valores de los ejes
        if i == minima: # Veo si la posicion de la caminata es la misma que la caminata con el maximo mas pequeño
            plt.plot(caminata, color='red', alpha=1) # Imprimo la caminata con el mismo color que la del grafico que tiena el maximo mas pequeño
        elif i == maxima: # Veo si la posicion de la caminata es la misma que la caminata con el maximo mas grande
            plt.plot(caminata, color='black', alpha=1) # Imprimo la caminata con el mismo color que la del grafico que tiena el maximo mas grande
        else:
            plt.plot(caminata, alpha=0.5) # dibuja las caminatas restantes
        plt.xticks([]) # No muestro los datos del eje x

    for caminata in mas_alejada:
        plt.subplot(2, 2, 3) # define la primera de abajo
        plt.title("La caminata que mas se aleja", color='green', fontname='Comic Sans MS', fontsize=11)
        plt.xlabel("Tiempo.", color='m')
        plt.ylabel("Distancia al Origen.", color='m')
        plt.ylim(-1000, 1000)
        ticks = [-1000, -500, 0, 500, 1000] # Seteo la escala de los valores de los ejes
        plt.yticks(ticks=ticks, fontsize=8, color='k') # Seteo la escala de los valores de los ejes
        plt.plot(caminata, color='black') # dibuja la caminata
        plt.xticks([]) # No muestro los datos del eje x
        
    for caminata in menos_alejada:
        plt.subplot(2, 2, 4) # define la segunda de abajo
        plt.title("La caminata que menos se aleja", color='green', fontname='Comic Sans MS', fontsize=11)
        plt.xlabel("Tiempo.", color='m')
        plt.ylabel("Distancia al Origen.", color='m', labelpad=5)
        plt.ylim(-1000, 1000)
        ticks = [-1000, -500, 0, 500, 1000] # Seteo la escala de los valores de los ejes
        plt.tick_params(right=True, left=False, labelleft=False, labelright=True) # Muevo de izquierda a derecha las etiquetas del eje
        plt.yticks(ticks=ticks, fontsize=8, color='k') # Seteo la escala de los valores de los ejes
        plt.plot(caminata, color='red') # dibuja la caminata
        plt.xticks([]) # No muestro los datos del eje x
    plt.show()

if __name__ == "__main__":
    graficar()
    
# Aclaración: El diseño del grafico puede verse diferente de acuerdo a la resolución del monitor,
#               puede que el texto de los ejes se vea dentro de una grafica,
#               Se soluciona al ponerlo en pantalla completa.
