class Canguro:
    def __init__(self, nombre, lista=[]):
        items = []
        self.nombre = nombre
        # Anterior: self.contenido_marsupio = lista
        for i in lista:
            items.append(i)
        self.contenido_marsupio = items

    def meter_en_marsupio(self, marsupio):
        self.contenido_marsupio.append(marsupio)
    
    def __str__(self):
        t = [self.nombre + ' tiene en su marsupio: ']
        for contenido in self.contenido_marsupio:
            s = '    ' + object.__str__(contenido)
            t.append(s)
        return '\n'.join(t)
    
    #def __repr__(self):
        #return f'Canguro ({self.nombre}, tiene {self.contenido_marsupio} en su marsupio)'
    
if __name__ == '__main__':    
    madre_canguro = Canguro('Madre')
    cangurito = Canguro('gurito')
    madre_canguro.meter_en_marsupio('billetera')
    madre_canguro.meter_en_marsupio('llaves del auto')
    madre_canguro.meter_en_marsupio(cangurito)
    cangurito.meter_en_marsupio('información')

    print(madre_canguro)
    print(cangurito)