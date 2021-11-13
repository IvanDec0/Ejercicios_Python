#%%
import csv
from fileparse import parse_csv
import csv

# Función Tomar costo de frutas y cantidad
# Ejercicio 6.11: Usemos tu módulo

def leer_camion(nombre_archivo_compra):
    """Lee un archivo .csv y crea un diccionario con Nombre-Cajones-Precio de compra dentro de una lista"""
    info_camion = parse_csv(nombre_archivo_compra, select = ['nombre', 'cajones', 'precio'], types = [str, int, float], has_headers = True)
    return(info_camion)

def leer_precios(nombre_archivo_venta):
    """Lee un archivo .csv y devuelve un diccionario Nombre-Precio de venta"""
    info_costo = parse_csv(nombre_archivo_venta, types = [str, float], has_headers = False)
    return(dict(info_costo))

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
    print('')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
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

if __name__ == '__main__':
    informe = informe_camion('../Data/camion.csv', '../Data/precios.csv')  
    imprimir = imprimir_informe(informe)

