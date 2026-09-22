# Ejemplo 1.19 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Verificar si un número natural positivo es fuerte, es decir, si la
# suma de los factoriales de sus dígitos es igual al número. Por
# ejemplo, 145 es fuerte porque 1! + 4! + 5! = 145.

N = int(input("Ingrese un número natural: "))
T = N
S = 0
while T > 0:
    D = T % 10
    F = 1
    for i in range(1, D + 1):
        F = F * i
    S = S + F
    T = T // 10
if S == N:
    print("Es un número fuerte")
else:
    print("No es un número fuerte")
