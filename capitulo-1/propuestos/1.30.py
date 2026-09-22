# Propuesto 1.30 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dados dos números naturales, determinar si son amigos: la suma de
# los divisores propios de cada uno es igual al otro.

A = int(input("Primer número: "))
B = int(input("Segundo número: "))
SA = 0
for C in range(1, A):
    if A % C == 0:
        SA = SA + C
SB = 0
for C in range(1, B):
    if B % C == 0:
        SB = SB + C
if SA == B and SB == A:
    print("Son amigos")
else:
    print("No son amigos")
