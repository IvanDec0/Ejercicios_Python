class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0
    
class TorreDeControl:
    
    def __init__(self):
        self.arribos = Cola()
        self.partidas = Cola()
        
    def nuevo_arribo(self, vuelo):
        self.arribos.encolar(vuelo) 
        
    def nueva_partida(self, vuelo):
        self.partidas.encolar(vuelo)
    
    def ver_estado(self):
        retorno = ''
        res_arribos = ", ".join(self.arribos.items)
        res_despegue = ", ".join(self.partidas.items)
        if not self.arribos.esta_vacia():
            aterizar = f'Vuelos esperando para aterrizar: {res_arribos}'
        if not self.partidas.esta_vacia():
            despegar = f'Vuelos esperando para despegar: {res_despegue}'
        retorno = f'{aterizar} \n{despegar}' 
        return retorno
    
    def asignar_pista(self):
        if self.arribos.esta_vacia() == False:
            vuelo = self.arribos.items.pop(0)
            print(f"El vuelo {vuelo} aterrizó con éxito." )
        elif self.partidas.esta_vacia() == False:
            vuelo = self.partidas.items.pop(0)
            print(f"El vuelo {vuelo} despegó con éxito." )
        else:
            print('No hay vuelos en espera.')