# Propuesto 2.18 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Leer un número de varios dígitos y mostrar una línea por cada
# dígito, tomados de derecha a izquierda, según la regla que se
# desprende del ejemplo: para N = 734265 las líneas son 12345,
# 666666, 22, 4444, 123 y 1234567.

def lineaAscendente(K):
    """Escribe en una línea los números de 1 hasta K."""
    for C in range(1, K + 1):
        print(C, end="")
    print()

def repetir(K):
    """Escribe en una línea el dígito K repetido K veces."""
    for C in range(1, K + 1):
        print(K, end="")
    print()


# --------------------------------- programa principal
N = int(input("Número de varios dígitos: "))
while N > 0:
    D = N % 10
    if D % 2 == 1:
        lineaAscendente(D)
    else:
        repetir(D)
    N = N // 10
