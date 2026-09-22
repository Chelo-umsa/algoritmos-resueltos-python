# Ejemplo 2.12 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Leer un número entre 1 y 9 y, si es válido, mostrar una secuencia
# de líneas donde la primera contiene el 1, la segunda del 1 al 2, y
# así hasta la última. Para N = 5 la salida son las líneas 1, 12,
# 123, 1234 y 12345.

def lineaAscendente(K):
    """Escribe en una línea los números de 1 hasta K."""
    for C in range(1, K + 1):
        print(C, end="")
    print()


# --------------------------------- programa principal
N = int(input("Ingrese un número entre 1 y 9: "))
if N < 1 or N > 9:
    print("Error: el número debe estar entre 1 y 9")
else:
    for C in range(1, N + 1):
        lineaAscendente(C)
