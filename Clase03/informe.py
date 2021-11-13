
# Ejercicio informe



import csv

ubicacion_archivo = '../Data/camion.csv'

# Abro archivo y declaro encabezado
def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        
        # Declaro variables
        precio_pagado = 0.0
        ncajones = 0
        precio = 0.0
        # Recorro archivo y realizo los correspondientes calculos
        print(headers)
        print('---------  '*3)
        for n_row, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                precio_pagado = precio_pagado + (ncajones * precio)
            # Esto atrapa errores en los int() y float() de arriba.
                print(row)
            except ValueError:
                print(f'Fila {n_row}: No pude interpretar: {row}')
        print('\n')
        return round(precio_pagado, 2)


# Declaro funcion main (En este caso no es necesario ya que el programa cuenta con una sola funcion)
def main():
    archivo = (ubicacion_archivo)
    costo = costo_camion(archivo)

    print(f'Costo total: ${costo}')


if __name__ == '__main__':
    main()
    



