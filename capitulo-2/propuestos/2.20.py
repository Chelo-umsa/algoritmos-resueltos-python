# Propuesto 2.20 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Leer un número de varios dígitos y mostrar la secuencia que se
# desprende del ejemplo: para N = 456143 las líneas son 7654321,
# 54321, 7654321, 1110987654321 y 987654321.

def lineaDescendente(K):
    """Escribe en una línea los números de K hasta 1."""
    for C in range(K, 0, -1):
        print(C, end="")
    print()


# --------------------------------- programa principal
N = int(input("Número de varios dígitos: "))
A = N % 10
N = N // 10
while N > 0:
    B = N % 10
    lineaDescendente(A + B)
    A = B
    N = N // 10
