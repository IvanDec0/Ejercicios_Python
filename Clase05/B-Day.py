import random

def paradoja(n):
    x = []
    for i in range(n):
        x.append(int(random.random()*365))
    for j in range(n):
        for k in range(n):
            if (x[j] == x[k] and j != k):
                return 1
    return 0

if __name__ == '__main__':
    n = 30
    p = 0
    bp = 0
    itera = 1000
    for i in range(itera):
        z = paradoja(n)
        if (z==1):
            p+=1
        else:
            bp+=1
    prom = (p/(p+bp))*100
    print(f'Probabilidad promedio de {prom:.2f}%')

