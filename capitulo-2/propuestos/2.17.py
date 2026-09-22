# Propuesto 2.17 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Leer un número entre 1 y 9 y mostrar una secuencia de líneas que
# empieza en 1 hasta N y se acorta de a un número. Si el número no
# es válido, mostrar un mensaje de error.

def lineaAscendente(K):
    """Escribe en una línea los números de 1 hasta K."""
    for C in range(1, K + 1):
        print(C, end="")
    print()


# --------------------------------- programa principal
N = int(input("Número entre 1 y 9: "))
if N < 1 or N > 9:
    print("Error: el número debe estar entre 1 y 9")
else:
    for C in range(N, 0, -1):
        lineaAscendente(C)
