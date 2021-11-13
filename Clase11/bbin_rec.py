def bbinaria_rec(lista, e, minimo=0, maximo=None):
    if len(lista) == 0:
        return False
    
    elif len(lista) == 1:
        return lista[0] == e
    
    else:
        if maximo == None:
            maximo = len(lista)-1
            lista.sort()
    # Si la lista tiene largo > 1 
        if maximo >= minimo:
    
            mid = (maximo + minimo) // 2
    
            # Si el elemento esta en el medio de la lista
            if lista[mid] == e:
                return True
    
            # Si el elemento es menor al medio
            elif lista[mid] > e:
                return bbinaria_rec(lista, e , minimo, mid - 1)
    
            # Si el elemento es mayor al medio
            else:
                return bbinaria_rec(lista, e, mid + 1, maximo)
    
        else:
            # Elemento no encontrado
            return False
    
print(bbinaria_rec([2, 3, 4, 10, 40] , 3)) 


