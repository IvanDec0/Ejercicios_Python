# Ejercicio Tabla_Informe

import csv

#Variables ubicaciones archivos
ubicacion_camion = '../Data/camion.csv'
ubicacion_precios = '../Data/precios.csv'



# Funcion calcular costo del camión
def costo_camion(nombre_archivo):
    costo_total = 0
    with open(nombre_archivo, encoding='utf-8') as f:
        encabezados = next(f).split(',') 
        for linea in f:                 
            elementos_fila = linea.split(',')
            total = float(elementos_fila[1]) * float(elementos_fila[2])
            costo_total += total    
    return costo_total

# Función Tomar costo de frutas y cantidad
def leer_camion(nombre_archivo):
    lista_dict = []
    with open(nombre_archivo, encoding='utf-8') as f:
        for linea in csv.DictReader(f):
            lista_dict.append(linea)
    return lista_dict

# Función abir archivo precios y tomar el precio venta de las frutas
def leer_precios(nombre_archivo):
    with open(nombre_archivo, encoding='utf-8') as f:
        return dict(filter(None, csv.reader(f))) 



data_precios = leer_precios(ubicacion_precios)
data_camion = leer_camion(ubicacion_camion)
# Funcion para realizar el informe
def hacer_informe(data_camion, data_precios):
    informe = []
    for fruta_descarga in data_precios:
        for fruta_camion in data_camion:
            if fruta_descarga == fruta_camion['nombre']:
                cambio = float(data_precios[fruta_descarga]) - float(fruta_camion['precio'])
                tupla = (fruta_camion['nombre'], int(fruta_camion['cajones']), float(fruta_camion['precio']), cambio)
                informe.append(tupla)
    return informe

# Mostrar la tabla de informe
informe = hacer_informe(data_camion, data_precios)
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print('█████████████'*4)
print(f'██{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>11s} {headers[3]:>12s}  ██')
print('█████████████'*4)
pesos = '$'
for nombre, cajones, precio, cambio in informe:
    print(f'██{nombre:>10s} █{cajones:>10d} █{pesos:>4s} {precio:>6.2f} █{cambio:10.2f} ██')
print('█████████████'*4)

camion = leer_camion(ubicacion_camion)
precios = leer_precios(ubicacion_precios)
informe = hacer_informe(camion, precios)

# A continuación, he realizado 2 dibujos con caracteres extradidos de comandos ascii
print('\n\n')

print('Camión de Frutas')
print(f'▄'*25)
print(f'█\tFrutas\t\t█   █▀▀▄╗(¤')
print('█'*25,'--█▄▄▀╝(¤')
print(f'{("(@)"):>3s}{("(@)"):>7s}{("(@)"):>12s}{("(@)"):>9s}')
print('▒'*40)
print('\n')

print('    __')
print('   (  )')
print('   |  |____        ╔═════════════╗ ')
print('---´   ____)       ║   Gracias   ║ ')
print('      (_____)    _ ║     por     ║ ')
print('      (_____)   /  ║     tu      ║ ')
print('      (____) __/   ║  Corrección ║ ')
print('---.__(___)        ╚═════════════╝ ')
print('\n\n')




