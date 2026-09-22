# Propuesto 1.33 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Obtener B elevado a P empleando únicamente sumas y restas.

B = int(input("Base: "))
P = int(input("Exponente: "))
R = 1
for C in range(1, P + 1):
    S = 0
    for i in range(1, B + 1):
        S = S + R
    R = S
print(R)
