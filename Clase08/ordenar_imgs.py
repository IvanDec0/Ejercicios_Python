#%%
import sys
import os
from datetime import datetime

def procesar_nombre(fname):
    try:
        os.mkdir(os.path.join('..', 'Data', 'imgs_procesadas'))
    except:
        pass
    directorio = os.path.join('..', 'Data', 'ordenar')
    procesadas = os.path.join('..','Data','imgs_procesadas')
    for root, dirs, files in os.walk(directorio):
        for name in dirs:
                if fname.endswith(('.png')):
                    fecha = datetime(year=int(fname[-12:-8]), month=int(fname[-8:-6]), day=int(fname[-6:-4])).strftime('%d/%m/%Y')
                    try:
                        renamed = os.rename(os.path.join(root, fname), os.path.join(procesadas, (fname[:-13]+fname[-4:])))
                    except:
                        continue
    for root, dirs, files in os.walk(directorio):
        for name in dirs:
                if fname.endswith(('.png')):
                    fecha = datetime(year=int(fname[-12:-8]), month=int(fname[-8:-6]), day=int(fname[-6:-4])).strftime('%d/%m/%Y')
                    try:
                        renamed = os.rename(os.path.join(root, name, fname), os.path.join(procesadas, (fname[:-13]+fname[-4:])))
                    except:
                        continue
    return fecha, renamed

def procesar(fname):
    fecha, renamed = procesar_nombre(fname)
    directorio = os.path.join('..', 'Data', 'ordenar')
    for root, dirs, files in os.walk(directorio):
        for name in dirs:
            os.rmdir()
    return fecha, renamed

def f_principal():
    '''
    f_principal [Toma los diferentes parametros que se le asignen a la funcion,
    ya sea por consola(CMD), o por ejecucion interna en el editor de codigo]
    '''
    if len(sys.argv) == 2:
        nombre = sys.argv[1]
        nombre = nombre.strip('\'')
    elif len(sys.argv) <= 2:
        raise SystemExit(f'El uso deberia ser {sys.argv[0]} + directorio')
    else:
        nombre = 'python_20190812.png'
    listado = procesar(nombre)
    return listado
    

if __name__ == '__main__':
    procesar_nombre('python_20190812.png')
    #print(f_principal())


# %%
directorio = os.path.join('..', 'Data', 'ordenar')
procesadas = os.path.join('..','Data','imgs_procesadas')
for datos in os.walk(directorio):
    dirs = datos[1]
    files = datos[2]
    for folders in dirs:
        print(folders)
# %%
