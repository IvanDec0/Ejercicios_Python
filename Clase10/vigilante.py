#%%
import os
import time

def vigilar(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF
    
    while True:
        line = f.readline()
        if line == '':        # línea vacía
            time.sleep(0.5)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        yield line   # devuelve la línea 

if __name__ == '__main__':
    for line in vigilar('../Data/mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        if volumen > 1000:
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')


# %%
