# Propuesto 3.13 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Leer dos vectores A y B del mismo tamaño y dos números t y r, y
# mostrar el vector tA + rB.

def leerVector(N, nombre):
    """Lee N elementos enteros desde el teclado."""
    V = [0] * N
    for i in range(N):
        V[i] = int(input(nombre + "[" + str(i) + "]: "))
    return V

def combinacion(A, B, t, r):
    """Devuelve el vector tA + rB."""
    C = [0] * len(A)
    for i in range(len(A)):
        C[i] = t * A[i] + r * B[i]
    return C


# --------------------------------- programa principal
N = int(input("Tamaño de los vectores: "))
A = leerVector(N, "A")
B = leerVector(N, "B")
t = int(input("Valor de t: "))
r = int(input("Valor de r: "))
print("tA + rB =", combinacion(A, B, t, r))
