# Ejemplo 2.3 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dado un número natural N de varios dígitos, mostrar cada uno de
# sus dígitos no primos, de izquierda a derecha. Por ejemplo, para N
# = 4275 la salida esperada es 4.

def invertir(N):
    """Devuelve N con sus dígitos invertidos."""
    T = N
    R = 0
    while T > 0:
        D = T % 10
        R = R * 10 + D
        T = T // 10
    return R


# ------------------------ definidos en ejemplos anteriores
def esPrimo(X):
    """Verdadero si X tiene exactamente dos divisores."""
    Q = 0
    for C in range(1, X + 1):
        if X % C == 0:
            Q = Q + 1
    return Q == 2


# --------------------------------- programa principal
N = int(input("Ingrese un número de varios dígitos: "))
T = invertir(N)
while T > 0:
    D = T % 10
    if not esPrimo(D):
        print(D)
    T = T // 10
