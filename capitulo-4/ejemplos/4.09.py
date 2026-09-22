# Ejemplo 4.9 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Calcular y mostrar la suma de los elementos de la diagonal
# principal y la suma de los de la diagonal secundaria de una matriz
# cuadrada de orden n que se ingresa elemento por elemento.

def crearNula(m, n):
    """Matriz de ceros de m filas y n columnas."""
    M = []
    for i in range(m):
        M.append([0] * n)
    return M

def leerMatriz(m, n, nombre):
    """Lee una matriz de m filas y n columnas."""
    M = crearNula(m, n)
    for i in range(m):
        for j in range(n):
            p = nombre + "[" + str(i) + "][" + str(j) + "]: "
            M[i][j] = int(input(p))
    return M

def sumaDiagonales(M):
    """Suma de la diagonal principal y de la secundaria."""
    n = len(M)
    P = 0
    S = 0
    for i in range(n):
        P = P + M[i][i]
        S = S + M[i][n - 1 - i]
    return P, S


# --------------------------------- programa principal
n = int(input("Orden de la matriz: "))
A = leerMatriz(n, n, "A")

P, S = sumaDiagonales(A)
print("Diagonal principal:", P)
print("Diagonal secundaria:", S)
