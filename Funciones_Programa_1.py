"""
Gallardo del Rosario Christian Pablo
Grupo 951
19 de Agosto de 2023
"""

"""
Ejercicio 1
Duplicados. Dada una lista de números enteros, retorna True si al menos 
un valor aparece dos veces, y Falso si todos los elementos son distintos.
"""


def Duplicados(Lista):
    numeros = set(Lista)
    return len(numeros) < len(Lista)


Lista1 = [1, 2, 3, 4, 5, 6, 1, 2, 2, 2, 2]
Lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(Duplicados(Lista1))
print(Duplicados(Lista2))
print("---FIN DEL EJERCICIO 1---")

"""
Ejercicio 2
Suma de dos números. Dado una lista de números enteros y 
un valor entero (target), retorna el índice de los dos números que 
sumados sean igual al target. Debe asumir que existe siempre una única 
solución, y que los elementos no se pueden usar dos veces. Debes retorna 
una tupla con los índices.
"""


def Busqueda_Suma(nums, target):
    num_indice = {}
    for i, num in enumerate(nums):
        completa = target - num
        if completa in num_indice:
            return (num_indice[completa], i)
        num_indice[num] = i
    return None


lista = [2, 7, 11, 15]
meta = 9
indice = Busqueda_Suma(lista, meta)
print(indice)
print("---FIN DEL EJERCICIO 2---")

"""
Ejercicio 3
Encriptar. Diseñe una función encripta(s, clave), que reciba un string s 
con un mensaje y un string con una clave de codificación, y retorne el 
mensaje codificado según la clave leída. Los signos de puntuación y dígitos 
que aparecen en el mensaje deben conservarse sin cambios. 
La clave consiste en una sucesión de las 26 letras minúsculas del alfabeto, 
las cuales se hacen corresponder con el alfabeto básico (a...z, sin la ñ o vocales acentuadas) 
de 26 letras. La primera letra de la clave se relaciona con la letra 'a', 
la segunda con la letra 'b', etc. Por ejemplo, una entrada de la forma:

Clave = 'ixmrklstnuzbowfaqejdcpvhyg' 
Texto para codificar: 'cafe'

"""

"""
Ejercicio 4
Desencriptar. Diseña una función desencripta(s, clave) que realice la función 
inversa a la función anterior, es decir, reciba un string s y una clave y realice 
la desencriptación del mensaje en el string devolviendo la cadena desencriptada. 

"""
def encripta(s, clave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()  # Convertir a minúsculas
    mensaje_codificado = ''

    for char in s:
        if char.isalpha():
            index = alfabeto.index(char)
            mensaje_codificado += clave[index]
        else:
            mensaje_codificado += char

    return mensaje_codificado

def desencripta(s, clave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    mensaje_desencriptado = ''

    for char in s:
        if char.isalpha():
            index = clave.index(char)
            mensaje_desencriptado += alfabeto[index]
        else:
            mensaje_desencriptado += char

    return mensaje_desencriptado

clave = 'ixmrklstnuzbowfaqejdcpvhyg'

mensaje_encriptado = encripta('cafe', clave)
print(mensaje_encriptado)

mensaje_encriptado = encripta('dame 1 chocolate', clave)
print(mensaje_encriptado)

mensaje_desencriptado = desencripta('milk', clave)
print(mensaje_desencriptado)

mensaje_desencriptado = desencripta('riok 1 mtfmfbidk', clave)
print(mensaje_desencriptado)
print("---FIN DEL EJERCICIO 3 Y 4---")

"""
Ejercicio 5
Gestión de Pensionistas. Crear una clase llamada GrupoPensionistas la cual tendrá un único atributo 
una lista o diccionario de objetos de tipo Pensionista (Elija a conveniencia si una lista o diccionario). 
Cada objeto de Pensionista tiene los siguientes atributos: identificador del pensionista (string), 
un entero que indica la edad y una serie de gastos mensuales que se guardan (lista de enteros). 
El número de gastos mensuales puede variar entre pensionistas. Por ejemplo, el pensionista con 
identificador '1111A' se llama 'Carlos' tiene 68 años y tiene 3 gastos mensuales de 640, 589 y 573. 
"""
class Pensionista:
    def __init__(self, identificador, edad, gastos_mensuales):
        self.identificador = identificador
        self.edad = edad
        self.gastos_mensuales = gastos_mensuales

    def calcular_promedio_gastos(self):
        return sum(self.gastos_mensuales) / len(self.gastos_mensuales)

class GrupoPensionistas:
    def __init__(self):
        self.pensionistas = []

    def agregar_pensionista(self, pensionista):
        self.pensionistas.append(pensionista)

    def mediaGastos(self, identificador):
        for pensionista in self.pensionistas:
            if pensionista.identificador == identificador:
                return pensionista.calcular_promedio_gastos()
        return None

    def mediaEdad(self):
        total_edades = sum(p.edad for p in self.pensionistas)
        return total_edades / len(self.pensionistas)

    def edadesExtremas(self):
        if not self.pensionistas:
            return None, None
        min_pensionista = min(self.pensionistas, key=lambda p: p.edad)
        max_pensionista = max(self.pensionistas, key=lambda p: p.edad)
        return min_pensionista, max_pensionista

    def sumaPromedio(self):
        total_promedios = sum(p.calcular_promedio_gastos() for p in self.pensionistas)
        return total_promedios

    def mediaMaxima(self):
        if not self.pensionistas:
            return None, None, None
        max_media = max(self.pensionistas, key=lambda p: p.calcular_promedio_gastos())
        return max_media.calcular_promedio_gastos(), max_media.identificador, max_media.edad

    def gastoPromedio(self):
        gastos_promedio = [p.calcular_promedio_gastos() for p in self.pensionistas]
        gastos_promedio.sort()
        return gastos_promedio

pensionista1 = Pensionista('1111A', 68, [640, 589, 573])
pensionista2 = Pensionista('2222B', 75, [800, 700, 900])
grupo_pensionistas = GrupoPensionistas()
grupo_pensionistas.agregar_pensionista(pensionista1)
grupo_pensionistas.agregar_pensionista(pensionista2)

print("Media de gastos de '1111A':", grupo_pensionistas.mediaGastos('1111A'))
print("Media de edades:", grupo_pensionistas.mediaEdad())
print("Edades extremas:", grupo_pensionistas.edadesExtremas())
print("Suma de promedios de gastos:", grupo_pensionistas.sumaPromedio())
print("Mayor promedio de gastos:", grupo_pensionistas.mediaMaxima())
print("Gasto promedio de cada persona:", grupo_pensionistas.gastoPromedio())
print("---FIN DEL EJERCICIO 5---")
"""
Ejercicio 6
Estadística Básica. Cree una clase llamada Estadística que contiene como atributo una lista de números naturales 
la cual puede contener repetidos. Debe contener los siguientes métodos:
Frecuencia de Números. Dada la lista, devuelve un diccionario con el número de veces que aparece cada número en la lista.
Moda. Dada la lista, devuelva la moda de la lista (el valor más repetido). Puedes usar la función anterior como ayuda.
Histograma. Dada la lista, muestra el histograma de la lista. Puedes reusar los métodos anteriores. 

"""
class Estadistica:
    def __init__(self, lista_numeros):
        self.lista_numeros = lista_numeros

    def frecuencia_numeros(self):
        frecuencias = {}
        for num in self.lista_numeros:
            if num in frecuencias:
                frecuencias[num] += 1
            else:
                frecuencias[num] = 1
        return frecuencias

    def moda(self):
        frecuencias = self.frecuencia_numeros()
        max_frecuencia = max(frecuencias.values())
        moda = [num for num, frecuencia in frecuencias.items() if frecuencia == max_frecuencia]
        return moda

    def histograma(self):
        frecuencias = self.frecuencia_numeros()
        for num, frecuencia in frecuencias.items():
            print(f"{num} {'*' * frecuencia}")

numeros = [1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1]
lista = Estadistica(numeros)

print("Frecuencia de Números:")
frecuencias = lista.frecuencia_numeros()
print(frecuencias)

print("\nModa:")
moda = lista.moda()
print(moda)

print("\nHistograma:")
lista.histograma()
print("---FIN DEL EJERCICIO 6---")