'''
Ejercicio Diccionario Geringoso
'''

# Declaro variables
d = {}
vocales = 'aeiou'
lista = ['banana', 'manzana', 'mandarina']

lista_geringoso = []
# Creo la función
def geringoso(text):
    geringoso1 = []
    # Transformo las palabras de la lista a Geringoso
    for c in text:
        if c in vocales:
            c = c +'p'+c
        geringoso1.append(c)
    return "".join(geringoso1)
# Creo una nueva lista con las palabras en geringoso    
for elemento in lista:
    lista_geringoso.append(geringoso(elemento))
# Agrego las palabras y las palabras en geringoso al diccionario
d = dict(zip(lista,lista_geringoso))
print(d)