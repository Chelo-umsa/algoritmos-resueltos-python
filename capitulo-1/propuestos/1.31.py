# Propuesto 1.31 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Mostrar los primeros N números perfectos.

N = int(input("Cantidad de perfectos: "))
C = 0
M = 1
while C < N:
    M = M + 1
    S = 0
    for i in range(1, M):
        if M % i == 0:
            S = S + i
    if S == M:
        print(M)
        C = C + 1
