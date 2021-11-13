# Ejercicio Tabla Multiplicar

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Imprime la primer linea de numeros(Numeros a multiplicar),
# en caso del primer numero,
# Le agrega un espacio para que quede bien alineado
for i in numeros:
    if i == numeros[0]:
        print(f' {i:>5d}',end='')   
    else: 
        print(f'{i:>5d}',end='')
print()
print('-'*53)
# Imprime los numeros de la primer columna (Numeros a multiplicar)
for i in numeros:
    print(f'{i:>1d} |', end='')
    for j in numeros:
        # Realiza la multiplicacion y la muestra
        print(f"{(i*j):>3d} |", end='')   
    print()
print('-'*53)
