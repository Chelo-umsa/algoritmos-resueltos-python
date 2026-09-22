# Propuesto 1.27 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dado un número natural de varios dígitos, mostrar sus dígitos que
# no son primos, de izquierda a derecha.

N = int(input("Número de varios dígitos: "))
R = 0
while N > 0:
    R = R * 10 + N % 10
    N = N // 10
while R > 0:
    D = R % 10
    Q = 0
    for i in range(1, D + 1):
        if D % i == 0:
            Q = Q + 1
    if Q != 2:
        print(D)
    R = R // 10
