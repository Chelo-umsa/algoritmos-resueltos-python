# Ejemplo 1.6 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Obtener el factorial de un número natural N, entendido como el
# producto de todos los naturales desde 1 hasta N. Por ejemplo, el
# factorial de 5 es 1 × 2 × 3 × 4 × 5 = 120.

N = int(input("Ingrese un número: "))
F = 1
for C in range(1, N + 1):
    F = F * C
print(f"El factorial de {N} es: {F}")
