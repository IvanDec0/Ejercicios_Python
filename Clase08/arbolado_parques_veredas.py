#%%
import pandas as pd
import os
import seaborn as sns

directorio = os.path.join('..','Data')
archivo_parque = 'arbolado-en-espacios-verdes.csv'
archivo_vereda = 'arbolado-publico-lineal-2017-2018.csv'
parqname = os.path.join(directorio,archivo_parque) # Archivo de parque
verename = os.path.join(directorio,archivo_vereda) # Archivo de veredas
df_parques = pd.read_csv(parqname) # DataFrame parque
df_veredas = pd.read_csv(verename) # DataFrame vereda

df_parques.rename(columns={'nombre_cie': 'nombre', 'altura_tot': 'altura'}, inplace=True) # Rename parque
df_veredas.rename(columns={'nombre_cientifico':'nombre', 'altura_arbol':'altura', 'diametro_altura_pecho':'diametro'}, inplace=True) # Rename veredas

cols = ['altura', 'diametro'] # Columnas a seleccionar

df_tipas_parques = df_parques[df_parques['nombre'] == 'Tipuana tipu'] # Selecciono las columnas de la especie
df_tipas_parques = df_parques[cols].copy() # Creo copia con los datos de las columnas seleccionadas
df_tipas_parques['ambiente'] = 'Parque' # Añado la columna 'ambiente'


df_tipas_veredas = df_veredas[df_veredas['nombre'] == 'Tipuana tipu'] # Selecciono las columnas de la especie
df_tipas_veredas = df_veredas[cols].copy() # Creo copia con los datos de las columnas seleccionadas
df_tipas_veredas['ambiente'] = 'Vereda' # Añado la columna 'ambiente'


df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques]) # Junto ambos DataSets
df_tipas.boxplot('diametro', by = 'ambiente').set_ylabel('Diámetro')

df_tipas.boxplot('altura', by = 'ambiente').set_ylabel('Altura')

# %%
