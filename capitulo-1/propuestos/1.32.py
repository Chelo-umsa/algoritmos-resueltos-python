# Propuesto 1.32 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Obtener el cociente y el resto de dividir dos números naturales
# empleando únicamente sumas.

A = int(input("Dividendo: "))
B = int(input("Divisor: "))
S = 0
Q = 0
while S + B <= A:
    S = S + B
    Q = Q + 1
R = 0
while S < A:
    S = S + 1
    R = R + 1
print("Cociente:", Q)
print("Resto:", R)
