# Ejemplo 1.21 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Mostrar por pantalla los primeros N números primos. Por ejemplo,
# para N = 4 la salida esperada es 2, 3, 5 y 7.

N = int(input("Ingrese la cantidad de primos que desea: "))
C = 0
M = 1
while C < N:
    M = M + 1
    Q = 0
    for i in range(1, M + 1):
        if M % i == 0:
            Q = Q + 1
    if Q == 2:
        print(M)
        C = C + 1
