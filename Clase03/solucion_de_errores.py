#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era que solo iteraba la primera letra de cada string,
# y tambien solo tomaba la letra 'a' y no 'A'... Estaba ubicado dentro del if,
# al iteral la primera letra devolvia True o False y no continuaba por las demas letras.
#    Lo corregí agregando un for dentro del while. Agregando (expresion[i] == 'A') en la sentencia if.
# y por ultimo elimine el else y en su lugar incremento la variable i, y si sale del for sin devolver True, devuelve False.
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        for i in range(n):
            if expresion[i] == 'a' or expresion[i] == 'A':
                return True
            i+=1
        return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))


# %%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de tipo Sintactico y estaba ubicado en el final de la declaracion de la funcion,
# del condicional del while, y el condicional del if
# Deltro del if falta un = para realizar la comparacion, y no toma en cuenta la letra 'A'
# Y por ultimo, el return Falso, no es correcto.
# Lo solucione agregando : al final de cada sentencia nombrada anteriomente.
# Dentro del if agrege (expresion[i] == 'A')
# Modifique return Falso por return False.

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))

# %%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era de tipo 'Type' y estaba ubicado en la llamada a la funcion con un int y no con un string
# Lo solucione preguntando si la expresion era type int, y transformandola a un string.



def tiene_uno(expresion):
    if type(expresion) == int:
        expresion = str(expresion)
        n = len(expresion)
    else:
        n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))

# %%
#Ejercicio 3.4. Función suma()
#Comentario: El error estaba ubicado en el final de la funcion, ya que no devolvia nada, y la suma (c), 
# se perdia

# Lo solucione agregando retun c.

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma de {a} + {b} = {c}")

# %%

#Ejercicio 3.5. Función leer_camion()
#Comentario: Error de tipo, pisado de memoria. 
# El error estaba ubicado en la declaracion del diccionario,
# debido a que en cada iteracion se guardaba el mismo valor, 
# pisando el resto de valores

# Lo solucione moviendo la ubicacion de registro={}, dentro del bloque for,
# para que en cada iteracion tome una nueva linea y no pise la anterior.

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

# %%
