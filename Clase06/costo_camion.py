import csv
from fileparse import parse_csv
from informe_funciones import leer_camion
import sys

def costo_camion(nombre_archivo):
    costo_total = 0
    info_camion = leer_camion(nombre_archivo)
    for linea, _ in enumerate(info_camion):                 
        total = int(info_camion[linea]['cajones']) * float(info_camion[linea]['precio'])
        costo_total += total   
    return costo_total


def f_principal(lista=[]):
    '''
    f_principal [Toma los diferentes parametros que se le asignen a la funcion,
    ya sea por consola(CMD), o por ejecucion interna en el editor de codigo]
    
    Lista = [] para que se le pueda llamar desde consola, interprete de python o desde el mismo editor de codigo.
    '''
    if len(sys.argv) == 2:
        archivo_camion = sys.argv[1]
        
    elif len(lista) > 0:
        archivo_camion = lista[1]
        
    else:
        archivo_camion = '../Data/camion.csv'
        
    return costo_camion(archivo_camion)
    


if __name__ == '__main__':
    Camion = f_principal()
    print(f'\nEl costo del camión de frutas es de: ${Camion}')
    print('\n\n')
    print(f'▄'*25)
    print(f'█\tFrutas\t\t█   █▀▀▄╗(¤')
    print('█'*25,'--█▄▄▀╝(¤')
    print(f'{("(@)"):>3s}{("(@)"):>7s}{("(@)"):>12s}{("(@)"):>9s}')
    print('▒'*40)
    print('\n')


# %%
