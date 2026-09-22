# Propuesto 1.40 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Mostrar la sumatoria de los primeros N términos de la serie −2/0!
# + 3/1! + 8/2! + 13/3! + 18/4! + …, es decir −2/1 + 3/1 + 8/2 +
# 13/6 + 18/24 + …, en la que los numeradores aumentan de cinco en
# cinco y los denominadores son los factoriales sucesivos.

N = int(input("Cantidad de términos: "))
S = 0
F = 1
for C in range(0, N):
    if C > 0:
        F = F * C
    S = S + (-2 + 5 * C) / F
print(S)
