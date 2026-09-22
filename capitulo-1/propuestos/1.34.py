# Propuesto 1.34 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Obtener B elevado a P empleando únicamente sumas, sin restas.

B = int(input("Base: "))
P = int(input("Exponente: "))
R = 1
C = 0
while C < P:
    S = 0
    i = 0
    while i < B:
        S = S + R
        i = i + 1
    R = S
    C = C + 1
print(R)
