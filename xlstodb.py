#importar librerias

import pandas as pd
import sqlite3 as sq

import glob
import os

#Definir lista de columnas para DF Principal
col_list = ["SubTotal", "Placa", "Fecha"]

#Juntar archivos excel dentro del folder para hacer merge
dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'archivos/')

all_files = glob.glob(path + "/*.xls")

li = []

for filename in all_files:
    df = pd.read_excel(filename, index_col=None, header=0, usecols=col_list)
    li.append(df)

puntos = pd.concat(li, axis=0, ignore_index=True)


#CREAR DATAFRAME
df = puntos.groupby(['Placa'])['SubTotal'].sum().reset_index()

table_name = "test"

conn = sq.connect('{}.sqlite'.format(table_name)) # creates file
df.to_sql(table_name, conn, if_exists='replace', index=False) # writes to file
conn.close() # good practice: close connection


