# Propuesto 1.39 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dado un número natural de varios dígitos, contar cuántas veces dos
# dígitos impares consecutivos tienen entre ellos al menos un dígito
# par.

N = int(input("Número de varios dígitos: "))
Q = 0
hayImpar = False
hayPar = False
while N > 0:
    D = N % 10
    if D % 2 == 1:
        if hayImpar and hayPar:
            Q = Q + 1
        hayImpar = True
        hayPar = False
    else:
        hayPar = True
    N = N // 10
print(Q)
