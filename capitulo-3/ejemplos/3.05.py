# Ejemplo 3.5 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Determinar la longitud de un vector V, entendida como la raíz
# cuadrada del producto escalar del vector consigo mismo.

import math

def leerVector(N, nombre):
    """Lee N elementos enteros desde el teclado."""
    V = [0] * N
    for i in range(N):
        V[i] = int(input(nombre + "[" + str(i) + "]: "))
    return V

def mostrar(V, titulo):
    """Escribe el vector precedido de un título."""
    print(titulo, V)

def productoEscalar(A, B):
    """Suma de los productos posición a posición."""
    S = 0
    for i in range(len(A)):
        S = S + A[i] * B[i]
    return S

def longitud(V):
    """Longitud: raíz del producto escalar consigo mismo."""
    return math.sqrt(productoEscalar(V, V))


# --------------------------------- programa principal
N = int(input("Tamaño del vector: "))
V = leerVector(N, "V")

mostrar(V, "Vector V:")
print("Longitud del vector:", longitud(V))
