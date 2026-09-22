# Ejemplo 2.14 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Leer un número impar entre 1 y 7 y mostrar una secuencia donde
# cada línea repite un mismo dígito tantas veces como indica su
# valor, de mayor a menor, empezando por N + 1. Para N = 5 la salida
# son las líneas 666666, 55555, 4444, 333, 22 y 1.

def repetir(K):
    """Escribe en una línea el dígito K repetido K veces."""
    for C in range(1, K + 1):
        print(K, end="")
    print()


# --------------------------------- programa principal
N = int(input("Ingrese un número impar entre 1 y 7: "))
if N < 1 or N > 7 or N % 2 == 0:
    print("Error: debe ser impar y estar entre 1 y 7")
else:
    for C in range(N + 1, 0, -1):
        repetir(C)
