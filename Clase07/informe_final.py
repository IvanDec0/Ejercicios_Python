#%%
from fileparse import parse_csv
import csv
import sys

# Ejercicio 7.7

# Función Tomar costo de frutas y cantidad
def leer_camion(archivo_camion):
    """Lee un archivo .csv y crea un diccionario con Nombre-Cajones-Precio de compra dentro de una lista"""
    with open(archivo_camion) as lineas:
        return parse_csv(lineas, select=['nombre', 'cajones', 'precio'], types=[str, int, float])


def leer_precios(archivo_precios):
    """Lee un archivo .csv y devuelve un diccionario Nombre-Precio de venta"""
    with open(archivo_precios) as lineas:
        return dict(parse_csv(lineas, types=[str, float], has_headers=False))


def informe_camion(archivo_camion, archivo_precios):
    """Lee dos archivos .csv y devuelve una lista con Nombre-Cajones-Precio de compra-Diferencia entre precio de venta y compra"""
    compra = leer_camion(archivo_camion)
    ventas = leer_precios(archivo_precios)
    informe = []
    for n_fila, fila in enumerate(compra):
        cajon = {
            'nombre': str(compra[n_fila]['nombre']),
            'cajones': int(compra[n_fila]['cajones']),
            'precio': float(compra[n_fila]['precio']),
            'diferencia': (round(float(ventas[compra[n_fila]['nombre']]) - float(compra[n_fila]['precio']), 2))
        }
        informe.append(cajon)
    return(informe)


def imprimir_informe(informe):
    '''
    imprimir_informe Imprime en pantalla el informe generado

    Args:
        informe ([Lista]): [Contiene 'Nombre', 'Precio', 'Cajones', 'cambio']
    '''
    headers = ['Nombre', 'Cajones', 'Precio', 'Cambio']
    print('')
    print(
        f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('-' *50)
    for n_fila, _ in enumerate(informe):
        nombre = informe[n_fila]['nombre']
        cajones = str(informe[n_fila]['cajones'])
        precio = (informe[n_fila]['precio'])
        precio_str = (f'${precio}')
        diferencia = (informe[n_fila]['diferencia'])
        diferencia_str = str(f'{"$":>4s}{diferencia:>2.2f}')
        print(f'{nombre:>10s} {cajones:>10s} {precio_str:>10s} {diferencia_str:>10s}')
    return()


def f_principal(lista=[]):
    '''
    f_principal [Toma los diferentes parametros que se le asignen a la funcion,
    ya sea por consola(CMD), o por ejecucion interna en el editor de codigo]
    
    Lista = [] para que se le pueda llamar desde consola, interprete de python o desde el mismo editor de codigo.
    '''
    if len(sys.argv) == 3:
        archivo_camion = sys.argv[1]
        archivo_precios = sys.argv[2]
    elif len(lista) > 0:
        archivo_camion = lista[1]
        archivo_precios = lista[2]
    else:
        archivo_camion = '../Data/camion.csv'
        archivo_precios = '../Data/precios.csv'
    informe = informe_camion(archivo_camion, archivo_precios)
    imprimir = imprimir_informe(informe)


if __name__ == '__main__':
    f_principal()


# %%
