# Ejemplo 1.17 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dado un número natural positivo, determinar si es perfecto. Un
# número es perfecto cuando la suma de sus divisores propios es
# igual al propio número, excluyéndolo de sí mismo. Por ejemplo, 6 =
# 1 + 2 + 3.

N = int(input("Ingrese un número natural: "))
S = 0
for C in range(1, N - 1 + 1):
    if N % C == 0:
        S = S + C
if S == N:
    print("Es un número perfecto")
else:
    print("No es un número perfecto")
