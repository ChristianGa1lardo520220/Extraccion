"""
Gallardo del Rosario Christian Pablo
Grupo 951
27 de Agosto de 2023
"""
import pandas
import pandas as pd
"""
Ejercicio 1
Escribir un programa que genere y muestre por pantalla un DataFrame
"""
print("\n----EJERCICIO 1----")
Df_ventas = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Ventas": [30500, 35600, 28300, 33900],
    "Gastos": [22000, 23400, 18100, 20700]
}

DF_ventas = pandas.DataFrame(Df_ventas)
print(DF_ventas)
print("----FIN DEL EJERCICIO 1----")
"""
Ejercicio 2
Escribir una función que reciba un DataFrame con el formato del ejercicio 
anterior, una lista de meses, y devuelva el balance (ventas - gastos) total 
en los meses indicados.
"""
print("\n----EJERCICIO 2----")
def Calcular_balance(df, meses):
    df_filtrar = df[df["Mes"].isin(meses)]
    balance_total = df_filtrar["Ventas"].sum() - df_filtrar["Gastos"].sum()
    return balance_total

meses_deseados = ["Enero", "Febrero"]
balance_t = Calcular_balance(DF_ventas, meses_deseados)
print(f"El balance total para los meses deseados son: {balance_t}")
print("----FIN DEL EJERCICIO 2----")

"""
Ejercicio 3
Construir una función que construya un DataFrame a partir del archivo con el 
formato anterior y devuelve otro DataFrame con el mínimo, el máximo y la media 
de cada columna.
"""
print("----EJERCICIO 3----")
def procesar_cotizaciones(archivo):
    DF_cotizacion = pd.read_csv(archivo, sep=';', decimal=',', thousands='.', index_col=0)
    return pd.DataFrame([DF_cotizacion.min(), DF_cotizacion.max(), DF_cotizacion.mean()], index=['Mínimo', 'Máximo', 'Media'])
print(procesar_cotizaciones("https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/cotizacion.csv"))

print("----FIN DEL EJERCICIO 3----")

"""
Ejercicio 4
Generar un DataFrame con los datos del archivo.
Mostrar por pantalla las dimensiones del DataFrame.
Mostrar el número de datos que contiene, los nombres de sus columnas.
Mostrar las 10 primeras filas y las 10 últimas filas.
Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
"""
print("\n----Generar un DataFrame con los datos del archivo----")
DF_Titanic = pd.read_csv("https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/titanic.csv")
print(DF_Titanic)

print("\n----Mostrar por pantalla las dimensiones del DataFrame----")
dimensiones = DF_Titanic.shape
print(f"Dimensiones del DataFrame{dimensiones}")

print("\n----Mostrar el número de datos que contiene, los nombres de sus columnas----")
num_datos = DF_Titanic.size
nombre_col = DF_Titanic.columns.tolist()
print(f"Numero de datos: {num_datos} \nNombre de columnas: {nombre_col}")

print("\n----Mostrar las 10 primeras filas y las 10 últimas filas----")
P_filas = DF_Titanic.head(10)
U_filas = DF_Titanic.tail(10)
print(f"10 primeras filas:\n {P_filas}, 10 ultimas filas:\n {U_filas}")

print("\n----Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron----")
P_sobrevive = (DF_Titanic["Survived"].sum()/len(DF_Titanic)) * 100
P_fallidos = 100 - P_sobrevive
print(f"Porcentaje sobrevivientes: {P_sobrevive}, \nPorcentaje Fallecidos: {P_fallidos}")

print("\n----Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase----")
P_sob_clase = DF_Titanic.groupby("Pclass")["Survived"].mean() * 100
print(f"Porcentaje de Sobrevivientes por clase: \n {P_sob_clase}")
print("----FIN EJERCICIO 4----")