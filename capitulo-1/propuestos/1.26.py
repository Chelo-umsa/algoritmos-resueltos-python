# Propuesto 1.26 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Generar los primeros N pares de números primos gemelos, es decir,
# pares de primos cuya diferencia es 2.

N = int(input("Cantidad de pares: "))
C = 0
M = 2
while C < N:
    M = M + 1
    Q1 = 0
    Q2 = 0
    for i in range(1, M + 3):
        if M % i == 0:
            Q1 = Q1 + 1
        if (M + 2) % i == 0:
            Q2 = Q2 + 1
    if Q1 == 2 and Q2 == 2:
        print("(", M, ",", M + 2, ")")
        C = C + 1
