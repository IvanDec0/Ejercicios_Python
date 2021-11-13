#%%
# Ejercicio 4.15
import csv
def leer_arboles(nombre_archivo):
    with open(nombre_archivo,'tr', encoding='utf-8', ) as af:
        registros=csv.reader(af)
        encabezados =next(registros)
        arboleda=[]
        for fila in registros:
            arboleda+=[dict(zip(encabezados,fila))]
        return arboleda

lista = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
print(lista)

#%%
# Ejercicio 4.16
import csv
def leer_arboles(nombre_archivo):
    with open(nombre_archivo,'rt', encoding='utf-8', ) as af:
        registros=csv.reader(af)
        encabezados =next(registros)
        arboleda=[]
        for fila in registros:
            arboleda+=[dict(zip(encabezados,fila))]
            if 'Jacarandá' == fila[7]:
                H=[float(arbol[3]) for arbol in registros] # Si utilizo (arbol['altura_tot']) no funciona

        return H


lista = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')

print(lista)



# %%
# Ejercicio 4.17
import csv
def leer_arboles(nombre_archivo):
    with open(nombre_archivo,'rt', encoding='utf-8', ) as af:
        registros=csv.reader(af)
        encabezados =next(registros)
        arboleda=[]
        for fila in registros:
            arboleda+=[dict(zip(encabezados,fila))]
            if 'Jacarandá' == fila[7]:
                H=[(float(arbol[3]), float(arbol[4])) for arbol in registros] # Si utilizo (arbol['altura_tot']) y (arbol['diametro']) no funciona

        return H


lista = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')

print(lista)

# %%
