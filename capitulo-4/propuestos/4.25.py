# Propuesto 4.25 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Generar y mostrar la matriz Zn, que tiene unos en la primera fila,
# en la última y en la diagonal secundaria. Para n = 4 es la que
# muestra la guía.

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

def matrizZ(n):
    """Unos en la primera y última fila y en la secundaria."""
    M = crearNula(n, n)
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or i + j == n - 1:
                M[i][j] = 1
    return M


# --------------------------------- programa principal
n = int(input("Orden de la matriz: "))
mostrarMatriz(matrizZ(n), "Matriz Z:")
