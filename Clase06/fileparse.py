import csv


def parse_csv(nombre_archivo, select=None, types=[str, int, float], has_headers=True,):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar el tipo de Archivo, y si se quiere que tenga encabezados o no
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo, en caso de que has_headers sea Verdadero
        if has_headers == True:
            encabezados = next(filas)
        else:
            pass

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
            if types:
                fila = [func(val) for func, val in zip(types, fila)]
            if not fila:    # Saltear filas vacías
                continue
            if indices:
                fila = [fila[index] for index in indices]

            # Armar el diccionario
            if has_headers == True:
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
            else:
                # En caso de que no tenga Encabezado, creo una tupla en lugar de diccionario
                registro = tuple(fila)
                registros.append(registro)

    return registros
