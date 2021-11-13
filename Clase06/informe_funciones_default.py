# Ejercicio Tabla_Informe
#%%
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
# Funcion para realizar el informe
def hacer_informe(data_camion, data_precios):
    informe = []
    for fruta_descarga in data_precios:
        for fruta_camion in data_camion:
            if fruta_descarga == fruta_camion['nombre']:
                cambio = float(data_precios[fruta_descarga]) - float(fruta_camion['precio'])
                tupla = (fruta_camion['nombre'], int(fruta_camion['cajones']), float(fruta_camion['precio']), cambio)
                informe.append(tupla)
    return informe

def informe_camion(nombre_archivo_compra, nombre_archivo_venta):
    """Lee dos archivos .csv y devuelve una lista con Nombre-Cajones-Precio de compra-Diferencia entre precio de venta y compra"""
    compra_productor = leer_camion(nombre_archivo_compra)
    ventas = leer_precios(nombre_archivo_venta)
    informe = []
    for n_fila, fila in enumerate(compra_productor):
        cajon = {
            'nombre' : str(compra_productor[n_fila]['nombre']),
            'cajones' : int(compra_productor[n_fila]['cajones']),
            'precio' : float(compra_productor[n_fila]['precio']),
            'diferencia' : (round(float(ventas[compra_productor[n_fila]['nombre']]) - float(compra_productor[n_fila]['precio']),2))
        }
        informe.append(cajon)
    return(informe)


def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    headers_azul = str("\033[;34m"+(f'{headers[0]:>10s}')+"\033[0;m")
    print('')
    print(f'{headers_azul:>8s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(('-' * 10 + ' ') * len(headers))
    for n_fila, fila in enumerate(informe):
        nombre = informe[n_fila]['nombre']
        cajones = str(informe[n_fila]['cajones'])
        precio = (informe[n_fila]['precio'])
        precio_str = str(f'{precio:>10.2f}')
        diferencia = (informe[n_fila]['diferencia'])
        diferencia_str = str(f'{diferencia:>10.2f}')     
        print(f'{nombre:>10s} {cajones:>10s} {precio_str:>10s} {diferencia_str:>10s}')
    return()

informe = informe_camion('../Data/camion.csv', '../Data/precios.csv')  
imprimir = imprimir_informe(informe)

#Ejercicio 6.5: Crear una función de alto nivel para la ejecución del programa

#informe_camion('../Data/camion2.csv', '../Data/precios.csv')

files = ['../Data/camion.csv', '../Data/camion2.csv']
for name in files:
    print(f'{name:-^43s}')
    print(informe_camion(name, '../Data/precios.csv'))



