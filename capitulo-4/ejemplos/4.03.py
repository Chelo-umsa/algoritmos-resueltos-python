# Ejemplo 4.3 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Generar y mostrar la matriz ajedrez de orden n, en la que los unos
# y los ceros se alternan como las casillas de un tablero.

def crearNula(m, n):
    """Matriz de ceros de m filas y n columnas."""
    M = []
    for i in range(m):
        M.append([0] * n)
    return M

def mostrarMatriz(M, titulo):
    """Escribe la matriz fila por fila, con un título."""
    print("\n" + titulo)
    for i in range(len(M)):
        print(M[i])

def ajedrez(n):
    """Devuelve la matriz ajedrez de orden n."""
    M = crearNula(n, n)
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                M[i][j] = 1
    return M


# --------------------------------- programa principal
n = int(input("Orden de la matriz: "))

mostrarMatriz(ajedrez(n), "Matriz ajedrez:")
