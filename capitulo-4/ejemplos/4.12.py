# Ejemplo 4.12 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Ingresar una matriz A de m filas y n columnas y presentar el
# vector V de m por n elementos obtenido al colocar consecutivamente
# la primera fila, la segunda, y así sucesivamente.

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

def matrizAVector(M):
    """Vector con las filas de M una tras otra."""
    n = len(M[0])
    W = [0] * (len(M) * n)
    for i in range(len(M)):
        for j in range(n):
            W[i * n + j] = M[i][j]
    return W


# --------------------------------- programa principal
m = int(input("Número de filas: "))
n = int(input("Número de columnas: "))
A = leerMatriz(m, n, "A")

print("Vector resultante:")
print(matrizAVector(A))
