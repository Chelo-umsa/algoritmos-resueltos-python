# Ejemplo 1.11 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dado un número natural de varios dígitos, mostrar cada uno de sus
# dígitos separadamente, de derecha a izquierda. Por ejemplo, para N
# = 4271 la salida esperada es 1, 7, 2 y 4.

N = int(input("Ingrese un número de varios dígitos: "))
while N > 0:
    D = N % 10
    print(D)
    N = N // 10
