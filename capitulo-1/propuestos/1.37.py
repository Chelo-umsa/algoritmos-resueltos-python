# Propuesto 1.37 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Mostrar los primeros N números triangulares en orden decreciente,
# sin usar la fórmula n(n + 1)/2.

N = int(input("Cantidad de triangulares: "))
T = 0
for C in range(1, N + 1):
    T = T + C
for C in range(N, 0, -1):
    print(T)
    T = T - C
