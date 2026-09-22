# Ejemplo 3.7 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dado un vector V de N elementos enteros positivos, calcular la
# desviación estándar de sus valores.

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

def suma(V):
    """Devuelve la suma de todos los elementos."""
    S = 0
    for i in range(len(V)):
        S = S + V[i]
    return S

def promedio(V):
    """Devuelve el promedio de los elementos."""
    return suma(V) / len(V)

def desviacionEstandar(V):
    """Devuelve la desviación estándar del vector."""
    M = promedio(V)
    S = 0
    for i in range(len(V)):
        S = S + (V[i] - M) * (V[i] - M)
    return math.sqrt(S / len(V))


# --------------------------------- programa principal
N = int(input("Tamaño del vector: "))
V = leerVector(N, "V")

mostrar(V, "Vector V:")
print("Promedio:", promedio(V))
print("Desviación estándar:", desviacionEstandar(V))
