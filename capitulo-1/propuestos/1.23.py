# Propuesto 1.23 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Leer dos números e imprimir sus primeros diez múltiplos comunes.

A = int(input("Primer número: "))
B = int(input("Segundo número: "))
Q = 0
M = 0
while Q < 10:
    M = M + 1
    if M % A == 0 and M % B == 0:
        print(M)
        Q = Q + 1
