# Ejemplo 1.22 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Mostrar por pantalla los primeros N elementos de la secuencia de
# Fibonacci, en la que cada término es la suma de los dos
# anteriores. La secuencia empieza en 0, 1, 1, 2, 3, 5, 8, … y
# continúa indefinidamente.

N = int(input("Ingrese la cantidad de términos: "))
A = 0
B = 1
for C in range(1, N + 1):
    print(A)
    S = A + B
    A = B
    B = S
