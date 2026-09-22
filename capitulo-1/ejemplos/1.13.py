# Ejemplo 1.13 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Convertir un número decimal a su equivalente en binario. Por
# ejemplo, para N = 13 el resultado es 1101.

N = int(input("Ingrese un número decimal: "))
B = 0
P = 1
while N > 0:
    D = N % 2
    B = B + D * P
    P = P * 10
    N = N // 2
print(f"El equivalente binario es {B}")
