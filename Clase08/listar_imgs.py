#%%
import sys
import os

def archivos_png(directorio):
    lista = []
    for datos in os.walk(directorio):
        dirs = datos[1]
        files = datos[2]
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg')):
                lista.append(file)
    return lista

def f_principal():
    '''
    f_principal [Toma los diferentes parametros que se le asignen a la funcion,
    ya sea por consola(CMD), o por ejecucion interna en el editor de codigo]
    '''
    if len(sys.argv) == 2:
        ubicacion = sys.argv[1]
        ubicacion = ubicacion.strip('\'')
    elif len(sys.argv) <= 2:
        raise SystemExit(f'El uso deberia ser {sys.argv[0]} + directorio')
    else:
        ubicacion = '../Data/ordenar'
    listado = archivos_png(ubicacion)
    return listado
    

if __name__ == '__main__':
    print(f_principal())

