# Ejemplo 1.12 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dado un número natural N de varios dígitos, obtener un nuevo
# número formado con los dígitos de N en orden invertido. Por
# ejemplo, para N = 4271 el resultado es 1724.

N = int(input("Ingrese un número de varios dígitos: "))
R = 0
while N > 0:
    D = N % 10
    R = R * 10 + D
    N = N // 10
print(f"El número invertido es {R}")
