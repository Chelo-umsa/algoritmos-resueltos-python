# Ejemplo 1.5 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Mostrar por pantalla los primeros N múltiplos de un número K. Por
# ejemplo, para N = 4 y K = 3 la salida esperada es 3, 6, 9 y 12.

print("Múltiplos de un número")
N = int(input("Ingrese la cantidad de múltiplos: "))
K = int(input("Ingrese el número: "))
print("Los múltiplos son: ")
for C in range(1, N + 1):
    M = K * C
    print(M)
