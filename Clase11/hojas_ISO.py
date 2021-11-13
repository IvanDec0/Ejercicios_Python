def medidas_hoja_A(N):
    """
    Devuelve el ancho y el largo de la hoja A(N), por recursión.
    Pre: N >= a 0.
    Pos: devuelve un tupla con el ancho y el largo de la hoja.
    """
    if N == 0:
        res = (841,1189)
    elif N == 1:
        res = (1189 // 2, 841)
    else:
        res = medidas_hoja_A(N-1)
        res =  (res[1] // 2, res[0])
    return res


if __name__ == "__main__":
    N = -1 # Lo utilizo solamente para que siempre entre al while
    while (N < 0) or (N >= 11):
        N = int(input('Ingrese un número de hoja: '))
        if N < 0 or N >= 11:
            print('Uso adecuado: ingrese un número entre 0 y 10')
    print(medidas_hoja_A(N))
