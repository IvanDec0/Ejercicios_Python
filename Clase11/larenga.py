def pascal(fila, columna):
    if columna == 0:
        return 1
    if fila == 0:
        return columna
    return int((fila * pascal(fila-1, columna-1)) / columna)
        



def imprimir(n=10):
    for i in range(n+1):
        fila = ''
        for k in range(i+1):
            fila += f' {pascal(i, k)}'
        print(f'|{fila:^40}|')
        print()

if __name__ == '__main__':        
    #print(pascal(5, 2))
    imprimir()


