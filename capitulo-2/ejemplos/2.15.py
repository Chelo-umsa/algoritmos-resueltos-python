# Ejemplo 2.15 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Leer un número de varios dígitos y, por cada uno de sus dígitos
# tomados de derecha a izquierda, mostrar una línea: ascendente si
# el dígito es par y descendente si es impar. Para N = 17845 las
# líneas son 54321, 1234, 12345678, 7654321 y 1.

def lineaDescendente(K):
    """Escribe en una línea los números de K hasta 1."""
    for C in range(K, 0, -1):
        print(C, end="")
    print()


# ------------------------ definidos en ejemplos anteriores
def lineaAscendente(K):
    """Escribe en una línea los números de 1 hasta K."""
    for C in range(1, K + 1):
        print(C, end="")
    print()


# --------------------------------- programa principal
N = int(input("Ingrese un número de varios dígitos: "))
T = N
while T > 0:
    D = T % 10
    if D % 2 == 0:
        lineaAscendente(D)
    else:
        lineaDescendente(D)
    T = T // 10
