# Propuesto 1.35 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Obtener la sumatoria de los factoriales de los primeros N
# elementos de la secuencia de Fibonacci.

N = int(input("Cantidad de términos: "))
A = 0
B = 1
S = 0
for C in range(1, N + 1):
    F = 1
    for i in range(1, A + 1):
        F = F * i
    S = S + F
    T = A + B
    A = B
    B = T
print(S)
