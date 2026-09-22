# Propuesto 1.28 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dado un número natural de varios dígitos, formar un nuevo número
# con sus dígitos primos en orden decreciente.

N = int(input("Número de varios dígitos: "))
M = 0
for C in range(9, 1, -1):
    Q = 0
    for i in range(1, C + 1):
        if C % i == 0:
            Q = Q + 1
    if Q == 2:
        T = N
        while T > 0:
            if T % 10 == C:
                M = M * 10 + C
            T = T // 10
print(M)
