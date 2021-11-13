frase = input('Ingrese una frase: ')
#frase = 'Todos somos programadores'
palabras = frase.split()
frase_i = ''
for palabra in palabras:
    if palabra[-2] == 'o':
        palabra = palabra[:-2] + 'e' + palabra[-1]
        frase_i = frase_i + ' ' + palabra
    elif palabra[-1] == 'o':
        palabra = palabra[:-1] + 'e' 
        frase_i = frase_i + ' ' + palabra
    else:
        palabra = palabra
        frase_i = frase_i + ' ' + palabra
print(frase_i)
