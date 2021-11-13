import informe_final
from vigilante import vigilar
from formato_tabla import crear_formateador
import csv

def elegir_columnas(rows, indices):
        columnas = ((row[index] for index in indices) for row in rows)
        return columnas

def cambiar_tipo(rows, types):
    tipo = ((func(val) for func, val in zip(types, row)) for row in rows)
    return tipo

def hace_dicts(rows, headers):
    dicts = (dict(zip(headers, row)) for row in rows)
    return dicts
        
def filtrar_datos(rows, nombres):
    filas = (fila for fila in rows if fila['nombre'] in nombres)
    return filas


def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def ticker(camion_file, log_file, fmt = 'txt'):
    formateador = crear_formateador(fmt)
    camion = informe_final.leer_camion(camion_file)
    rows = parsear_datos(vigilar(log_file))
    rows = filtrar_datos(rows, camion)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for row in rows:
        nombre = row['nombre']
        precio = str(row['precio'])
        volumen = str(row['volumen'])
        rowdata = [nombre, precio, volumen]
        formateador.fila(rowdata)
    
if __name__ == '__main__':
    ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'txt')    
# %%
