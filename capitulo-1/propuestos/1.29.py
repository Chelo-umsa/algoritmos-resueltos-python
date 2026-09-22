# Propuesto 1.29 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Determinar si un número natural es automórfico, es decir, si su
# cuadrado termina en el mismo número.

N = int(input("Número natural: "))
C = N * N
P = 1
T = N
while T > 0:
    P = P * 10
    T = T // 10
if C % P == N:
    print("Es automórfico")
else:
    print("No es automórfico")
