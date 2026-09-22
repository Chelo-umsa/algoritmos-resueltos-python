# Ejemplo 1.18 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dado un número natural mayor que 1, determinar si es primo, es
# decir, si sus únicos divisores son el 1 y él mismo.

N = int(input("Ingrese un número natural mayor que 1: "))
Q = 0
for C in range(1, N + 1):
    if N % C == 0:
        Q = Q + 1
if Q == 2:
    print("Es un número primo")
else:
    print("No es un número primo")
