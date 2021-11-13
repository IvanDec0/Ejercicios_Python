#%%
# Ejercicio 4.5 Invertir lista
def invertir_lista(lista):
    invertida = [] #  Declaro la variable para guardar la lista invetida
    i = len(lista) # Declaro 1 variable con el largo de la lista
    for j in lista: # Recorro la lista
        i = i -1
        invertida.append(lista[i]) # Guardo el elemento de lista en Invertida
    return invertida

print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))
# %%
