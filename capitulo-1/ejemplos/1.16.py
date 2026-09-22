# Ejemplo 1.16 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dado un número natural N de varios dígitos, obtener un nuevo
# número M formado por los dígitos de N pero en orden creciente. Por
# ejemplo, para N = 4271 el resultado es 1247.

N = int(input("Ingrese un número de varios dígitos: "))
M = 0
for C in range(0, 10):
    T = N
    while T > 0:
        D = T % 10
        if D == C:
            M = M * 10 + D
        T = T // 10
print(f"El nuevo número es {M}")
