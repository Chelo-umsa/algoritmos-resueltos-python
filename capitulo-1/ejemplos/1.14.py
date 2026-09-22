# Ejemplo 1.14 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Convertir un número binario a su equivalente decimal. Por ejemplo,
# para B = 1101 el resultado es 13.

B = int(input("Ingrese un número binario: "))
S = 0
P = 1
while B > 0:
    D = B % 10
    S = S + D * P
    P = P * 2
    B = B // 10
print(f"El equivalente decimal es {S}")
