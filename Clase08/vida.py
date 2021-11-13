from datetime import datetime

def vida_en_segundos(fecha_nac):
    fecha_nac = datetime.strptime(fecha_nac, '%d/%m/%Y')
    hoy = datetime.now()
    print(hoy)
    dif_fecha = hoy - fecha_nac
    dif_fecha = dif_fecha.seconds + dif_fecha.days * 86400 # Segundos en un dia, se podria hacer 24 * 3600
    return dif_fecha

if __name__ == '__main__':
    print(f'{vida_en_segundos("21/09/2022")} segundos')
