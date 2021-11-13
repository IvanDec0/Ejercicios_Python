#%%
# Ejercicio 5.1
import random
def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6)) 

    return tirada

def es_generala(tirada):
    return all(x==tirada[0] for x in tirada)

if __name__ == '__main__':
    N = 100000
    G = sum([es_generala(tirar(5)) for i in range(N)])
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

# %%
#Ejercicio 5.2

import random
def tirar(n):
    tirada=[]
    for i in range(n):
        tirada.append(random.randint(1,6)) 
    return tirada

def es_generala(tirada):
    return all(x==tirada[0] for x in tirada)


def prob_generala():
    numero_tirada = 2 
    dados = 5
    lista = tirar(dados)
    mayor = 1
    numero = lista[0]

    #Este bloque hace la primera tirada y escoge el numero
    #del que queremos hacer generala    
    
    for i in range(5):
        if (lista.count(lista[i])) > mayor:
            numero = lista[i] # numero a buscar
            mayor = lista.count(lista[i]) # cantidad de veces
    dados_restantes = 5 - mayor

    
    while numero_tirada <= 3:
        numero_tirada += 1
        lista_temp = tirar(dados_restantes)
        if lista_temp.count(numero) > 0:
            dados_restantes -= (lista_temp.count(numero))
        

    if dados_restantes == 0:
        return True
    return False
        
# Partes de codigo de la función prob_generala, son de Kadyr Valdes

if __name__ == '__main__':
        
    N = 100000
    G = sum([es_generala(tirar(5)) for i in range(N)])
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
    
    F = sum([prob_generala() for i in range(N)])
    prob = F/N
    print(f'Tiré {N} veces, de las cuales {F} saqué generala.')
    print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')
# %%
