# Ejemplo 2.2 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dado un número natural N de varios dígitos, mostrar cada uno de
# sus dígitos primos, de derecha a izquierda. Por ejemplo, para N =
# 4275 la salida esperada es 5, 7 y 2.

def esPrimo(X):
    """Verdadero si X tiene exactamente dos divisores."""
    Q = 0
    for C in range(1, X + 1):
        if X % C == 0:
            Q = Q + 1
    return Q == 2


# --------------------------------- programa principal
N = int(input("Ingrese un número de varios dígitos: "))
T = N
while T > 0:
    D = T % 10
    if esPrimo(D):
        print(D)
    T = T // 10
