import numpy as np

Lista = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10]]
n1 = np.array(Lista)
print(n1)

print(type(n1))

#Principales atributos
print("----Principales Atributos----")
print(n1.ndim)
print(n1.shape)
print(n1.size)
print(n1.dtype)

#Acceso a los elementos
print("----Acceso a los elementos----")
print(n1[1,2]) #Primer numero es el renglon, segundo numero es la columna

print(n1 * 2)

print(np.linalg.norm(n1))
print(n1.T)
print(n1.mean())
print(n1[0, :].mean())

print("----Ecuaciones----")
"""
Ecuaciones
x + 2y = 1
3x + 5y = 2
"""
ecuaciones = [[1,2], [3,5]]

np_ecuaciones = np.array(ecuaciones)
res = np.array([1,2])
print(np.linalg.solve(np_ecuaciones, res))