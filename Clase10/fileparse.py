import csv

def parse_csv(lineas, select=None, types=[str, int, float], has_headers=True, delimiter=',', silence_errors = False):
    '''
    parse_csv [Parsea un archivo CSV en una lista de registros.]

    Args:
        lineas ([Archivo csv, listas, o tipos de archivos iterables]): [lee lo ingresado, siempre que sea iterable]
        select ([Lista], optional): [Selecciona las diferentes columnas, siempre que tenga encabezados]. Default es None.
        types (Lista, optional): [Lista con los diferentes tipos de datos ingresados]. Default es [str, int, float].
        has_headers (bool, optional): [Se selecciona si tiene encabezados o no]. Default es True.
        delimiter (str, optional): [Se selecciona el separador de los datos]. Default es ','.
        silence_errors (bool, optional): [Se selecciona si se quiere mostrar los errores o no]. Default es False.

    Returns:
        [Diccionario / Tupla]: [Devuelve un diccionario en caso de que tenga encabezados,
                                y en caso contrario se devuelve una tupla]
    '''
    
    if select and not has_headers and not silence_errors:
        raise RuntimeError('Para seleccionar, necesito encabezados')
    
    filas = csv.reader(lineas, delimiter=delimiter)

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
    for i, fila in enumerate(filas):
        try:
            if types:
                fila = [func(val) for func, val in zip(types, fila)]
            if not fila:    # Saltear filas vacías
                continue
            if indices:
                fila = [fila[index] for index in indices]
        except ValueError as e:
            if silence_errors == False:
                print(f"Faltan datos en el archivo en la fila {i} que contiene los datos {fila}.")
                print(f'Motivo: {e}\n')
                continue
            else:
                continue
                

            # Armar el diccionario
        if has_headers == True:
            registro = dict(zip(encabezados, fila))
            registros.append(registro)
        else:
            # En caso de que no tenga Encabezado, creo una tupla en lugar de diccionario
            registro = tuple(fila)
            registros.append(registro)
    return registros

