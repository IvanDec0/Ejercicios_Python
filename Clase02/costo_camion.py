'''
Ejercicio Costo_Camion
'''


import csv

ubicacion_archivo = "../Data/camion.csv"
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
        for row in rows:
            cajones = int(row[1])
            precio = float(row[2])
            precio_pagado = precio_pagado + (cajones * precio)
            print(row)
        return round(precio_pagado, 2)


# Declaro funcion main (En este caso no es necesario ya que el programa cuenta con una sola funcion)
def main():
    archivo = (ubicacion_archivo)
    costo = costo_camion(archivo)
    print('Costo total: $', costo)

if __name__ == '__main__':
    main()
    



