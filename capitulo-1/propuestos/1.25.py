# Propuesto 1.25 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dado un número natural de varios dígitos, mostrar sus dígitos
# primos de derecha a izquierda.

N = int(input("Número de varios dígitos: "))
while N > 0:
    D = N % 10
    Q = 0
    for i in range(1, D + 1):
        if D % i == 0:
            Q = Q + 1
    if Q == 2:
        print(D)
    N = N // 10
