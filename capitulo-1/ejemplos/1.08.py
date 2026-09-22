# Ejemplo 1.8 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Obtener el resultado de elevar una base B a un exponente entero no
# negativo E.

B = int(input("Ingrese la base: "))
E = int(input("Ingrese el exponente: "))
P = 1
for C in range(1, E + 1):
    P = P * B
print(f"La potencia es {P}")
