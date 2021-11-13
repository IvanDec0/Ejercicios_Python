'''
Ejercicio Hipoteca
Iván Décima
'''

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
adelanto_mes = 1000.0
mes_comienzo = 61
mes_fin = 108

while saldo > 0:
    mes = mes + 1
    if pago_mensual > saldo * (1+tasa/12):
        pago_mensual = saldo * (1+tasa/12)
    if mes >= mes_comienzo and mes <= mes_fin:
        saldo = saldo * (1+tasa/12) - pago_mensual - adelanto_mes
        total_pagado = total_pagado + pago_mensual + adelanto_mes       
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual            
    print("Mes", mes, "Pagado hasta el momento:" ,round(total_pagado, 2), "Saldo restante:" ,round(saldo, 2))
    
    
print('Total pagado', round(total_pagado, 2),"en", mes, "meses")



'''
VERSION 1.8

while saldo > 0:
    if (mes < 12):
        saldo = saldo * (1+tasa/12) - pago_mensual - adelanto_mes
        total_pagado = total_pagado + pago_mensual + adelanto_mes      
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual      
    mes = mes + 1    
    print("Mes", mes, "Pagado hasta el momento:" ,round(total_pagado, 2), "Saldo restante:" ,round(saldo, 2))
    
    
print('Total pagado', round(total_pagado, 2),"en", mes, "meses")
'''

'''
VERSION 1.9 - 1.10

while saldo > 0:
    if (mes >= mes_comienzo and mes <= mes_fin):
        saldo = saldo * (1+tasa/12) - pago_mensual - adelanto_mes
        total_pagado = total_pagado + pago_mensual + adelanto_mes
        
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual     
         
    mes = mes + 1    
    print("Mes", mes, "Pagado hasta el momento:" ,round(total_pagado, 2), "Saldo restante:" ,round(saldo, 2))
    
    
print('Total pagado', round(total_pagado, 2),"en", mes, "meses")

'''