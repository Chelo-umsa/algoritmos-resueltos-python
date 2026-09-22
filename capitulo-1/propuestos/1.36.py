# Propuesto 1.36 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Mostrar los primeros N números primos en orden decreciente.

N = int(input("Cantidad de primos: "))
C = 0
M = 1
while C < N:
    M = M + 1
    Q = 0
    for i in range(1, M + 1):
        if M % i == 0:
            Q = Q + 1
    if Q == 2:
        C = C + 1
for K in range(M, 1, -1):
    Q = 0
    for i in range(1, K + 1):
        if K % i == 0:
            Q = Q + 1
    if Q == 2:
        print(K)
