'''
Ejercicio Costo_Camion con eleccion de archivo y solución en caso de faltar algun campo del archivo
'''


import csv
import sys


# Abro archivo y declaro encabezado
def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        # Declaro variables
        precio_pagado = 0
        cajones = 0
        precio = 0
        # Recorro archivo y realizo los correspondientes calculos
        try:
            for row in rows:
                cajones = int(row[1])
                precio = float(row[2])
                precio_pagado = precio_pagado + (cajones * precio)
                print(row)
            return round(precio_pagado, 2)
        except:
            # Recorro el archivo
            for row in rows:
                # Pregunto si el campo 0 del archivo esta vacio, y si lo esta le asigno 'Fruta Desconocida'
                if (row[0]) == '':
                    precio_pagado = precio_pagado + int(row[1]) * float(row[2])
                    print(row)
                    print('WARNING: Falta el nombre de la fruta')
                # Pregunto si el campo 1 del archivo esta vacio, y si lo esta le asigno 0
                elif (row[1]) == '':
                    print(row)
                    print('WARNING: Faltan los cajones de ' + row[0])
                    
                    # Pregunto si el campo 2 del archivo esta vacio, y si lo esta le asigno 0
                elif (row[2]) == '':
                    print(row)
                    print('WARNING: Falta el precio de ' + row[0])
                # En caso de que ningun campo este vacio
                else:
                    precio_pagado = precio_pagado + int(row[1]) * float(row[2])
                    print(row)
            return round(precio_pagado, 2)




# Declaro funcion main (En este caso no es necesario ya que el programa cuenta con una sola funcion)
def main():
    if len(sys.argv) == 2:
        nombre_archivo = sys.argv[1]
    else:
        nombre_archivo = '../Data/camion.csv'
    costo = costo_camion(nombre_archivo)
    print('Costo total: $', costo)

if __name__ == '__main__':
    main()
    



