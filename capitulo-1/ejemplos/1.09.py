# Ejemplo 1.9 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Obtener el factorial de un número empleando únicamente sumas, sin
# usar el operador de multiplicación.

N = int(input("Ingrese un número: "))
F = 1
for C in range(2, N + 1):
    S = 0
    for i in range(1, C + 1):
        S = S + F
    F = S
print(f"El factorial es {F}")
