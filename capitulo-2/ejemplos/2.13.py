# Ejemplo 2.13 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Leer un número entre 1 y 9 y mostrar una pirámide de dígitos. Para
# N = 5 la salida son las líneas 1, 212, 32123, 4321234 y 543212345.

def lineaPiramide(K):
    """Escribe de K a 1 y luego de 2 a K."""
    for C in range(K, 0, -1):
        print(C, end="")
    for C in range(2, K + 1):
        print(C, end="")
    print()


# --------------------------------- programa principal
N = int(input("Ingrese un número entre 1 y 9: "))
if N < 1 or N > 9:
    print("Error: el número debe estar entre 1 y 9")
else:
    for C in range(1, N + 1):
        lineaPiramide(C)
