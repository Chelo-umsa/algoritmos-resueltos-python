# Propuesto 1.24 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dado un número natural de varios dígitos, mostrar sus dígitos
# pares de derecha a izquierda.

N = int(input("Número de varios dígitos: "))
while N > 0:
    D = N % 10
    if D % 2 == 0:
        print(D)
    N = N // 10
