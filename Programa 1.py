"""
Gallardo del Rosario Christian Pablo Gallardo del Rosario
Grupo 951
Martes 15 de Agosto de 2023
"""

"""
Ejercicio 1
Duplicados. Dada una lista de números enteros, retorna True si al menos 
un valor aparece dos veces, y Falso si todos los elementos son distintos.
"""

def Duplicados(Lista):
    numeros = set(Lista)
    return len(numeros) < len(Lista)
Lista1 = [1,2,3,4,5,6,1,2,2,2,2]
Lista2 = [1,2,3,4,5,6,7,8,9]
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
            return (num_indice[completa], i )
        num_indice[num] = i
    return None
    
lista = [2,7,11,15]
meta = 9
indice = Busqueda_Suma(lista, meta)
print(indice)
print("---FIN DEL EJERCICIO 2")

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
def encripta(s, clave):
    abc = {
        "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7,
        "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15,
        "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23,
        "y": 24, "z": 25
    }

    # Crear un diccionario inverso para mapear índices a letras en la clave
    inv_abc = {v: k for k, v in abc.items()}

    # Convertir la clave a minúsculas y eliminar espacios
    clave = clave.lower().replace(" ", "")

    mensaje_encriptado = ""
    for letra in s:
        if letra.isalpha():
            # Encontrar el índice en el abc original
            idx = abc[letra]
            # Encontrar la letra correspondiente en la clave
            letra_encriptada = inv_abc[(abc[clave[idx]] - abc['a']) % 26]
            mensaje_encriptado += letra_encriptada
        else:
            mensaje_encriptado += letra

    return mensaje_encriptado

# Ejemplos de uso
mensaje1 = 'cafe'
clave1 = 'ixmrklstnuzbowfaqejdcpvhyg'
print(encripta(mensaje1, clave1))  # Debería imprimir 'milk'

mensaje2 = 'dame 1 chocolate'
clave2 = 'ixmrklstnuzbowfaqejdcpvhyg'
print(encripta(mensaje2, clave2))  # Debería imprimir 'riok 1 mtfmfbidk'
print("----FIN DEL EJERCICIO 3----")
    
"""
Ejercicio 4
Desencriptar. Diseña una función desencripta(s, clave) que realice la función 
inversa a la función anterior, es decir, reciba un string s y una clave y realice 
la desencriptación del mensaje en el string devolviendo la cadena desencriptada. 

"""
