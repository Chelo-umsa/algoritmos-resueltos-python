# Propuesto 3.14 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Calcular el ángulo entre dos vectores no nulos U y V, sabiendo que
# su coseno es el producto escalar dividido entre el producto de sus
# longitudes.

import math

def leerVector(N, nombre):
    """Lee N elementos enteros desde el teclado."""
    V = [0] * N
    for i in range(N):
        V[i] = int(input(nombre + "[" + str(i) + "]: "))
    return V

def productoEscalar(A, B):
    """Suma de los productos posición a posición."""
    S = 0
    for i in range(len(A)):
        S = S + A[i] * B[i]
    return S

def longitud(V):
    """Longitud: raíz del producto escalar consigo mismo."""
    return math.sqrt(productoEscalar(V, V))

def angulo(U, V):
    """Devuelve el ángulo entre U y V, en grados."""
    c = productoEscalar(U, V) / (longitud(U) * longitud(V))
    return math.degrees(math.acos(c))


# --------------------------------- programa principal
N = int(input("Tamaño de los vectores: "))
U = leerVector(N, "U")
V = leerVector(N, "V")
print("Ángulo:", round(angulo(U, V), 2), "grados")
