#%%
# Arboles 3.18
import csv
def leer_parque(archivo,parque):
    with open(archivo,'tr', encoding='utf-8', ) as af:
        registros=csv.reader(af)
        encabezados =next(registros)
        lista_arbolado=[]
        i = 0
        for fila in registros:
            try:
               if parque == fila[10] or parque=='*':  # * para todos los parques
                lista_arbolado+=[dict(zip(encabezados,fila))]
                i = i + 1
            except:
                print('error de lectura')
        print(f'La cantidad de especies de arboles es: {i}')
        return(lista_arbolado)

leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')


#%%
# Arboles 3.19
import csv
# Funcion leer parque
def leer_parque(archivo,parque):
    with open(archivo,'tr', encoding='utf-8', ) as af:
        registros=csv.reader(af)
        encabezados =next(registros)
        lista_arbolado=[]
        # Variable para contar cantidad de arboles
        i = 0
        # Recorro el archivo y si el nombre del parque corresponde,
        # Se une al diccionario
        for fila in registros:
            try:
               if parque == fila[10] or parque=='*':  # * para todos los parques
                lista_arbolado+=[dict(zip(encabezados,fila))]
                i = i + 1
            except:
                print('error de lectura')
        print(f'La cantidad de especies de arboles es: {i}')
        return(lista_arbolado)

lista = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')

# Funcion especies
def especies(lista_arboles):
    arboles = []
    # Recorro el archivo, y la ubicacion, si existe o corresponde,
    # se une al diccionario
    for arbol in lista_arboles:
        uno = arbol['nombre_com']
        arboles.append(uno)
    especie = set(arboles)
    return especie

arboles = especies(lista)
print(arboles)


# %%

# Arboles 3.20
import csv
from collections import Counter
# Funcion leer parque
def leer_parque(archivo,parque):
    with open(archivo,'tr', encoding='utf-8', ) as af:
        registros=csv.reader(af)
        encabezados =next(registros)
        lista_arbolado=[]
        # Variable para contar cantidad de arboles
        i = 0
        # Recorro el archivo y si el nombre del parque corresponde,
        # Se une al diccionario
        for fila in registros:
            try:
               if parque == fila[10] or parque=='*':  # * para todos los parques
                lista_arbolado+=[dict(zip(encabezados,fila))]
                i = i + 1
            except:
                print('error de lectura')
        print(f'La cantidad de especies de arboles es: {i}')
        return(lista_arbolado)

# Gracias a Raimundo por ayudarme con esta función
# Funcion Contar ejemplares de un parque
def contar_ejemplares(lista_arboles):
    ejemplares_x_especie = Counter()
    for row in lista_arboles:
        try:
            ejemplares_x_especie[row['nombre_com']] +=  len(row['nombre_com'])
        except:
                pass
    return ejemplares_x_especie

# Llamo a la funcion de leer parque, con los 3 parques seleccionados
especies_genepaz = leer_parque('../Data/arbolado-en-espacios-verdes.csv', "GENERAL PAZ")
especies_andes = leer_parque('../Data/arbolado-en-espacios-verdes.csv', "ANDES, LOS")
especies_centenario = leer_parque('../Data/arbolado-en-espacios-verdes.csv', "CENTENARIO")

#especies_total = leer_parque('../Data/arbolado-en-espacios-verdes.csv', "*")


# Selecciono los 5 ejemplares o especies con mayor abundancia en cada parque
esp_frec_genePaz = contar_ejemplares(especies_genepaz).most_common(5)
esp_frec_andes = contar_ejemplares(especies_andes).most_common(5)
esp_frec_centenario = contar_ejemplares(especies_centenario).most_common(5)

#esp_frec_total = contar_ejemplares(especies_total).most_common(5)


# Muestro los 5 ejemplares/especies y su cantidad del parque GENERAL PAZ
print('-----------')
print('GENERAL PAZ')
print('-----------')
for i in range(0,5):    
    print(esp_frec_genePaz[i])


# Muestro los 5 ejemplares/especies y su cantidad del parque LOS ANDES
print('-----------')
print('LOS ANDES')
print('-----------')
for i in range(0,5):    
    print(esp_frec_andes[i])

    
# Muestro los 5 ejemplares/especies y su cantidad del parque CENTENARIO
print('-----------')
print('CENTENARIO')
print('-----------')
for i in range(0,5):    
    print(esp_frec_centenario[i])


'''print('-----------')
print('Total Bs As')
print('-----------')
for i in range(0,5):    
    print(esp_frec_total[i])'''


# %%
