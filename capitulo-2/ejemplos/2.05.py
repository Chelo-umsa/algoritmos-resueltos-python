# Ejemplo 2.5 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dado un número natural N de varios dígitos, obtener un nuevo
# número M formado por los dígitos primos de N pero en orden
# decreciente. Por ejemplo, para N = 4275 el resultado es 752.

# ------------------------ definidos en ejemplos anteriores
def esPrimo(X):
    """Verdadero si X tiene exactamente dos divisores."""
    Q = 0
    for C in range(1, X + 1):
        if X % C == 0:
            Q = Q + 1
    return Q == 2

def veces(N, C):
    """Cuántas veces aparece el dígito C en N."""
    T = N
    Q = 0
    while T > 0:
        D = T % 10
        if D == C:
            Q = Q + 1
        T = T // 10
    return Q


# --------------------------------- programa principal
N = int(input("Ingrese un número de varios dígitos: "))
M = 0
for C in range(9, -1, -1):
    if esPrimo(C):
        for i in range(1, veces(N, C) + 1):
            M = M * 10 + C
print(f"El nuevo número es {M}")
