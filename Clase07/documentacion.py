def valor_absoluto(n):
    '''
    valor_absoluto [Calcula el valor absoluto, de 'n'. Retorna el V.Absoluto de dicho número]

    Args:
        n ([Entero / Flotante]): [Número entero o flotante, positivo o negativo]

    Returns:
        [Entero / Flotante]: [devuelve el valor_absoluto de 'n' [un número entero o flotante,
                                                                positivo o negativo]]
    '''    
    if n >= 0:
        return n
    else:
        return -n
    
def suma_pares(l):
    '''
    suma_pares [Se ingresa una lista de Enteros / Flotantes como parametro,
                                            y se suman solo los numeros pares de dicha lista]

    Args:
        l ([Lista de Enteros / Flotantes]): [Lista de Enteros / Flotantes]

    Returns:
        [Entero / Flotante]: [Devuelve el resultado de la suma de numeros pares]
    '''    
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

def veces(a, b):
    '''
    veces [Toma 2 numeros enteros, y suma 'a' la cantidad de veces de 'b', y retorna el resultado]

    Args:
        a ([Entero]): [Numero entero positivo o negativo]
        b ([Entero]): [Número entero >= 0]

    Returns:
        [Entero]: [Suma de 'a' la cantidad de veces de 'b', (multiplicar 'a' * 'b')]
    '''    
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

def collatz(n):
    '''
    collatz [El numeros ingresesado como parametro, si es par se lo divide por 2,
            si es impar se lo multiplica por 3 y se le suma 1, 
            realizando dichas acciones con los diferentes resultados obtenidos,
            hasta que se llega a 1 y se corta la iteación]

    Args:
        n ([Entero]): [Se ingresa un número entero positivo como parametro]

    Returns:
        [Entero]: [Devuelve la cantidad de iteraciones que realizo 'n' hasta llegar a 1]
        
    Inv:
        n (Debe ser un número positivo)
    '''    
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res



