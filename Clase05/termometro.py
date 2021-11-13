#%%
# Ejercicio 5.6
import random
def medir_temp(n):
    lista =  []
    temp_real = 37.5
    for _ in range(n):
        # Guardo la variacion de temperatura generada de forma aleatoria
        result = float(f'{random.normalvariate(temp_real,0.2):.2f}')
        lista.append(result)
    return lista


def resumen_temp(n):
    # Declaración de Variables
    datos = []
    G = 0
    h = medir_temp(n)
    h.sort()
    tam = len(h)
    # Calculo la mediana
    # Si el tamaño de lista es impar, se calcula de la siguiente forma
    if (tam%2 > 0):
        # La mediana es el numero que se encuentra en el centro de la lista
        mediana = h[tam//2]
    # Si el tamaño de la lista es par, se calcula de la siguiente forma
    else:
        # Busco los 2 numeros en el centro de la lista
        num1 = h[tam//2]
        num2 = h[tam//2 - 1]
        # Calculo la mediana, sumando los 2 numeros y dividiendolos por 2
        mediana = float(f'{((num1 + num2)/2):.2f}')

    for i in h:
        G = G + i
    # Calculo el promedio mediante los valores que toma i y, que son guardados y sumados en G 
    prom = float(f'{(G/n):.2f}')
    # Agrego los valores a una lista
    datos.append(max(h))
    datos.append(min(h))
    datos.append(prom)
    datos.append(mediana)
    # Agrego los valores a la tupla
    tupla_datos = tuple(datos)
    
    return tupla_datos
        
if __name__ == '__main__':
    print(resumen_temp(10))



#%%
# Ejercicio 5.8
import random
import numpy as np
def medir_temp(n):
    lista =  []
    temp_real = 37.5
    for _ in range(n):
        # Guardo la variacion de temperatura generada de forma aleatoria
        result = float(f'{random.normalvariate(temp_real,0.2):.2f}')
        lista.append(result)
    # Guardo los resusltados en un archivo
    np.save('../Data/temperaturas.npy', lista)
    return lista

a = medir_temp(999)


b = np.load('../Data/temperaturas.npy')
print(b)


# %%
