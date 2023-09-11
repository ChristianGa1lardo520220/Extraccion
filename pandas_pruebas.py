import pandas
import pandas as pd

datos = {
    "Nombres":["Maria", "Luis", "Carmen"],
    "Examen":["Matematicas", "Programacion", "Mercadotecnia"],
    "Promedios": [80,90,100]
}

df_alumnos = pandas.DataFrame(datos)
print(df_alumnos)

df_colesterol = pd.read_csv("http://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv", sep = ";", decimal = ",")

#print(df_colesterol)
#print(df_colesterol.head())
#print(df_colesterol.sample(5))
#print(df_colesterol.info())
#print(df_colesterol.describe())
"""
print(df_colesterol.shape)
print(df_colesterol.size)
print(df_colesterol.columns)
print(df_colesterol.dtypes)
print(df_colesterol.index)
"""
#print(df_colesterol[["nombre", "edad", "colesterol"]])
df_colesterol["colesterol"].plot()