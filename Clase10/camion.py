class Camion:

    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()
    
    def __contains__(self, nombre):
        return any(lote.nombre == nombre for lote in self.lotes)

    def precio_total(self):
        return sum(l.costo() for l in self.lotes)

    def contar_cajones(self):  # Intento fallido al hacerla con Expresion Generadora
        from collections import Counter
        cantidad_total = Counter()
        for lote in self.lotes:
            cantidad_total[lote.nombre] += lote.cajones
        return cantidad_total
    
    def __len__(self):
        return len(self.lotes)
        
    def __getitem__(self,a):
        return self.lotes.__getitem__(a)
    
    def __repr__(self):
        return f'Camion ({self.lotes})'
    
        
    def __str__(self):
        cantidad = len(self.lotes)
        retorno = f'Camion con {cantidad} lotes: ' + '\n'
        info = ('   '+str(datos) for datos in self.lotes)
        retorno += '\n'.join(info)
        return retorno
    
