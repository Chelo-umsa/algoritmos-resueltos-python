# Ejemplo 2.4 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dado un número natural N de varios dígitos, obtener un nuevo
# número M formado por los dígitos de N pero en orden creciente. Por
# ejemplo, para N = 4271 el resultado es 1247.

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
for C in range(0, 10):
    for i in range(1, veces(N, C) + 1):
        M = M * 10 + C
print(f"El nuevo número es {M}")
