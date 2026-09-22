# Ejemplo 1.20 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Mostrar los factores primos de un número natural. Por ejemplo,
# para N = 60 la salida esperada es 2, 2, 3 y 5.

N = int(input("Ingrese un número natural: "))
D = 2
while N > 1:
    if N % D == 0:
        print(D)
        N = N // D
    else:
        D = D + 1
