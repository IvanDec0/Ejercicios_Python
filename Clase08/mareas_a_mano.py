import pandas as pd
import os


filename = os.path.join('..', 'Data', 'OBS_SHN_SF-BA.csv')
df = pd.read_csv(filename, index_col=['Time'], parse_dates=True)

dh = df['12-25-2014':].copy()

delta_t = -1 # tiempo que tarda la marea entre ambos puertos
delta_h = 16.5 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot().set_xlabel('Fecha')