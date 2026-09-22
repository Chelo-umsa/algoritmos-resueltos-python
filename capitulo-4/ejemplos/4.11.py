# Ejemplo 4.11 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Ingresar una matriz de m filas y n columnas y presentar el valor y
# la posición de su elemento máximo. Si hubiera varios máximos,
# presentar la posición del último leído.

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

def maximoMatriz(M):
    """Devuelve el mayor elemento y su fila y columna.

    Si hay varios máximos informa el último encontrado.
    """
    V = M[0][0]
    f = 0
    c = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] >= V:
                V = M[i][j]
                f = i
                c = j
    return V, f, c


# --------------------------------- programa principal
m = int(input("Número de filas: "))
n = int(input("Número de columnas: "))
A = leerMatriz(m, n, "A")

V, f, c = maximoMatriz(A)
print("Máximo:", V)
print("Fila", f, "y columna", c)
