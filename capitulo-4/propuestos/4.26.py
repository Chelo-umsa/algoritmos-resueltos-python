# Propuesto 4.26 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Generar y mostrar la matriz Hn, numerada de uno en uno recorriendo
# sus diagonales secundarias desde el ángulo superior izquierdo.
# Para n = 3 las filas son 1 2 4, 3 5 7 y 6 8 9.

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

def matrizH(n):
    """Numera recorriendo las diagonales secundarias."""
    M = crearNula(n, n)
    k = 1
    for s in range(2 * n - 1):
        for i in range(n):
            j = s - i
            if j >= 0 and j < n:
                M[i][j] = k
                k = k + 1
    return M


# --------------------------------- programa principal
n = int(input("Orden de la matriz: "))
mostrarMatriz(matrizH(n), "Matriz H:")
