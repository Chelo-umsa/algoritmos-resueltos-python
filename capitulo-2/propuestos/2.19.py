# Propuesto 2.19 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Leer un número de varios dígitos y mostrar la secuencia que se
# desprende del ejemplo: para N = 743941 las líneas son 123, 12345,
# 123456, 1 y 123.

def lineaAscendente(K):
    """Escribe en una línea los números de 1 hasta K."""
    for C in range(1, K + 1):
        print(C, end="")
    print()


# --------------------------------- programa principal
N = int(input("Número de varios dígitos: "))
A = N % 10
N = N // 10
while N > 0:
    B = N % 10
    D = A - B
    if D < 0:
        D = -D
    lineaAscendente(D)
    A = B
    N = N // 10
