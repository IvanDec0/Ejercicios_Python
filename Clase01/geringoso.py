'''
Ejercicio Geringoso
'''

'''
cadena = input("Ingrese una palabra: ") # En caso de que el programa sea para cualquier palabra, deberia correrse esta linea
#cadena = 'Geringoso' #En caso de que el programa sea solo para la palabra 'Geringoso', deberia correrse esta linea 
cadenafinal = ''
for c in cadena:
    cadenafinal += c
    if c in 'Aa':
        cadenafinal += "pa"
    if c in 'Ee':           
        cadenafinal += 'pe' 
    if c in 'Ii':               
        cadenafinal += 'pi'     
    if c in 'Oo':
        cadenafinal += 'po'   
    if c in 'Uu':
        cadenafinal += 'pu'
print(cadenafinal)
'''
cadena = input("Ingrese una palabra: ")
cadenafinal = ''
for c in cadena:
    cadenafinal += c
    if c in 'AaEeIiOoUu':
        cadenafinal += 'p'
        cadenafinal += c
print(cadenafinal)
        

