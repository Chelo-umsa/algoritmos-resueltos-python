# Ejemplo 1.7 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Obtener el producto de dos números naturales empleando únicamente
# sumas, es decir, sin usar el operador de multiplicación.

M = int(input("Ingrese el multiplicando: "))
N = int(input("Ingrese el multiplicador: "))
P = 0
for C in range(1, N + 1):
    P = P + M
print(f"El producto es {P}")
