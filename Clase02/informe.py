'''
Ejercicio Informe
'''

import csv

#Variables ubicaciones archivos
ubicacion_camion = '../Data/camion.csv'
ubicacion_precios = '../Data/precios.csv'



# Funcion calcular costo del camión
def costo_camion(nombre_archivo):
    costo_total = 0
    with open(nombre_archivo, encoding='utf-8') as f:
        encabezados = next(f).split(',') 
        for linea in f:                 
            elementos_fila = linea.split(',')
            total = float(elementos_fila[1]) * float(elementos_fila[2])
            costo_total += total    
    return costo_total

# Función Tomar costo de frutas y cantidad
def leer_camion(nombre_archivo):
    lista_dict = []
    with open(nombre_archivo, encoding='utf-8') as f:
        for linea in csv.DictReader(f):
            lista_dict.append(linea)
    return lista_dict

# Función abir archivo precios y tomar el precio venta de las frutas
def leer_precios(nombre_archivo):
    with open(nombre_archivo, encoding='utf-8') as f:
        return dict(filter(None, csv.reader(f))) 


data_precios = leer_precios(ubicacion_precios)
data_camion = leer_camion(ubicacion_camion)
# Recorrer archivo para calcular dinero ganado
dinero_ganado = 0
for each in data_camion:
    a_buscar = each.get('nombre')
    if a_buscar in data_precios:
        resultado = float(data_precios.get(a_buscar)) * float(each.get('cajones'))
        dinero_ganado += resultado
# Calcular inversión (Costo) y ganancia
dinero_invertido = costo_camion(ubicacion_camion)
ganancia = dinero_ganado - dinero_invertido

# Mostrar Costo y Ganancia
print(f'Costo del camión {dinero_invertido:0.2f} pesos')
if ganancia > 0:
    print(f'Tuve una ganancia de {ganancia:0.2f} pesos')
else:
    print(f'Tuve una perdida de {ganancia:0.2f} pesos')
