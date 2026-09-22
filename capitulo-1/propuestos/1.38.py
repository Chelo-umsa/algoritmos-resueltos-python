# Propuesto 1.38 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Obtener el máximo común divisor de dos números naturales.

A = int(input("Primer número: "))
B = int(input("Segundo número: "))
while B != 0:
    R = A % B
    A = B
    B = R
print(A)
