# Ejemplo 4.22 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Se dirá aquí que una matriz cuadrada de orden n forma un cuadrado
# mágico cuando la suma de cada fila, de cada columna y de las dos
# diagonales dé el mismo valor. Ingresar una matriz cuadrada y
# determinar si cumple esa condición.

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

def mostrarMatriz(M, titulo):
    """Escribe la matriz fila por fila, con un título."""
    print("\n" + titulo)
    for i in range(len(M)):
        print(M[i])

def sumaDiagonales(M):
    """Suma de la diagonal principal y de la secundaria."""
    n = len(M)
    P = 0
    S = 0
    for i in range(n):
        P = P + M[i][i]
        S = S + M[i][n - 1 - i]
    return P, S

def totalesPorFila(M):
    """Devuelve un vector con la suma de cada fila."""
    F = [0] * len(M)
    for i in range(len(M)):
        S = 0
        for j in range(len(M[i])):
            S = S + M[i][j]
        F[i] = S
    return F

def totalesPorColumna(M):
    """Devuelve un vector con la suma de cada columna."""
    n = len(M[0])
    C = [0] * n
    for j in range(n):
        S = 0
        for i in range(len(M)):
            S = S + M[i][j]
        C[j] = S
    return C

def esMagico(M):
    """Verdadero si todo suma lo mismo."""
    F = totalesPorFila(M)
    C = totalesPorColumna(M)
    P, S = sumaDiagonales(M)
    objetivo = F[0]
    for i in range(len(F)):
        if F[i] != objetivo or C[i] != objetivo:
            return False
    return P == objetivo and S == objetivo


# --------------------------------- programa principal
n = int(input("Orden de la matriz: "))
A = leerMatriz(n, n, "A")

mostrarMatriz(A, "Matriz A:")
if esMagico(A):
    print("Es un cuadrado mágico")
else:
    print("No es un cuadrado mágico")
