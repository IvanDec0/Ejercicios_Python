#%% ejercicio 7.7
import fileparse
import formato_tabla
import lote


def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    with open(nombre_archivo) as f:
        camion_dicts = fileparse.parse_csv(f, select = ['nombre', 'cajones', 'precio'], types = [str, int, float], has_headers = True)
        camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return camion

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = fileparse.parse_csv(f, types = [str, float], has_headers = False)
    return precios

def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        cambio = (precios[lote['nombre']] - lote['precio'])
        t = (lote['nombre'], lote['cajones'], lote['precio'], cambio)
        lista.append(t)
    return lista

def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    precios = dict(leer_precios(archivo_precios))

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # Imprime el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)

def f_principal(lista=[]):
    '''
    f_principal [Toma los diferentes parametros que se le asignen a la funcion,
    ya sea por consola(CMD), o por ejecucion interna en el editor de codigo]
    
    Lista = [] para que se le pueda llamar desde consola, interprete de python o desde el mismo editor de codigo.
    '''
    if len(sys.argv) == 4:
        archivo_camion = sys.argv[1]
        archivo_precios = sys.argv[2]
        formato = sys.argv[3]
        # En caso de pasar los parametros con (') comillas
        archivo_camion = archivo_camion.strip('\'')
        archivo_precios = archivo_precios.strip('\'')
        formato = formato.strip('\'')
    elif len(lista) > 0:
        archivo_camion = lista[1]
        archivo_precios = lista[2]
    else:
        archivo_camion = '../Data/camion.csv'
        archivo_precios = '../Data/precios.csv'
        formato = 'txt'
    informe_camion(archivo_camion, archivo_precios, formato)

if __name__ == '__main__':
    import sys
    f_principal()
    


# %%
