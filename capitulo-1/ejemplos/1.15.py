# Ejemplo 1.15 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dado un número natural de varios dígitos, determinar si es
# capicúa, es decir, si se lee igual de izquierda a derecha que de
# derecha a izquierda. Por ejemplo, 1221 es capicúa.

N = int(input("Ingrese un número de varios dígitos: "))
T = N
R = 0
while T > 0:
    D = T % 10
    R = R * 10 + D
    T = T // 10
if N == R:
    print("Es capicúa")
else:
    print("No es capicúa")
