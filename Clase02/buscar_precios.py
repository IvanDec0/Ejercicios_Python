'''
Ejercicio Busca_Precio
'''


import csv

ubicacion_archivo = "../Data/precios.csv"
# Abro archivo y declaro encabezado
def busca_precios(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        # Declaro variables
        contador = 0
        fruta = input('Ingrese la fruta que sea buscar: ')
        # Recorro archivo y busco si la fruta existe en el listado
        try:
            for row in rows:
                frutas = str(row[0])
                precio = float(row[1])
                if fruta in frutas:
                    # Muestro la fruta encontrada con el correspondiente precio
                        mensaje = (f'El precio de un cajon de {fruta} es de {precio}')
                        return mensaje
        except IndexError:
            # Muestro que la fruta no fue encontrada 
            mensaje = ('Fruta no encontrada')
            return mensaje                               

# Declaro funcion main (En este caso no es necesario ya que el programa cuenta con una sola funcion)
def main():
    archivo = (ubicacion_archivo)
    print (busca_precios(archivo))

if __name__ == '__main__':
    main()
    



