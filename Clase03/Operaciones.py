def suma(a,b):
    c= 0
    c = a + b
    return c

def resta(a,b):
    c= 0
    c = a - b
    return c

def multiplicacion(a,b):
    c= 0
    c = a * b
    return c

def division(a,b):
    c= 0
    c = a / b
    return c

def operacion():
    n1 = int(input('Ingrese el primer numero: '))
    n2 = int(input('Ingrese el segundo numero: '))

    opc = int(input(''' 
    1 - Suma
    2 - Resta
    3 - Multiplicación
    4 - División
    Ingrese que operación desea realizar: '''))
    
    if opc == 1:
        result = suma(n1,n2)
        print(f'El resultado de {n1} + {n2} es {result}')

    elif opc == 2:
        result = resta(n1,n2)
        print(f'El resultado de {n1} - {n2} es {result}')

    elif opc == 3:
        result = multiplicacion(n1,n2)
        print(f'El resultado de {n1} * {n2} es {result}')

    elif opc == 4:
        result = division(n1,n2)
        print(f'El resultado de {n1} / {n2} es {result}')

    else:
        print('\nNo existe una operacion asignada a ese numero\n\n')

def main():
    operacion()

if __name__ == '__main__':
    main()


