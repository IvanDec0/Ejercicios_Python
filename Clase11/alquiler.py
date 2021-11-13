import numpy as np
import matplotlib.pyplot as plt

def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

def graficar(x, y):
    a, b = ajuste_lineal_simple(x, y)
    
    minx = min(x)
    maxx = max(x)

    grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
    grilla_y = grilla_x*a + b

    g = plt.scatter(x = x, y = y, c='r', marker='*')
    plt.title('y ajuste lineal')
    plt.plot(grilla_x, grilla_y,'c--')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()
    
    return a, b


superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

a, b = graficar(superficie, alquiler)

errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())

