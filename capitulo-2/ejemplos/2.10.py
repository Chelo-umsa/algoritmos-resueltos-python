# Ejemplo 2.10 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Mostrar los primeros N números primos en orden decreciente. Por
# ejemplo, para N = 4 la salida esperada es 7, 5, 3 y 2.

def enesimoPrimo(N):
    """Devuelve el primo que ocupa la posición N."""
    Q = 0
    M = 1
    while Q < N:
        M = M + 1
        if esPrimo(M):
            Q = Q + 1
    return M


# ------------------------ definidos en ejemplos anteriores
def esPrimo(X):
    """Verdadero si X tiene exactamente dos divisores."""
    Q = 0
    for C in range(1, X + 1):
        if X % C == 0:
            Q = Q + 1
    return Q == 2


# --------------------------------- programa principal
N = int(input("Ingrese la cantidad de primos: "))
M = enesimoPrimo(N)
for C in range(M, 1, -1):
    if esPrimo(C):
        print(C)
