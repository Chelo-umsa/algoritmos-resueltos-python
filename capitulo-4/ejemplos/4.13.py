# Ejemplo 4.13 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Leer una matriz de m filas y n columnas. Construir el vector F de
# m elementos formado por los máximos de cada fila, y el vector C de
# n elementos formado por los máximos de cada columna.

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

def mayorVector(V):
    """Devuelve el mayor elemento de un vector no vacío."""
    M = V[0]
    for i in range(1, len(V)):
        if V[i] > M:
            M = V[i]
    return M

def maximosPorFila(M):
    """Devuelve un vector con el mayor de cada fila."""
    F = [0] * len(M)
    for i in range(len(M)):
        F[i] = mayorVector(M[i])
    return F

def maximosPorColumna(M):
    """Devuelve un vector con el mayor de cada columna."""
    n = len(M[0])
    C = [0] * n
    for j in range(n):
        C[j] = M[0][j]
        for i in range(1, len(M)):
            if M[i][j] > C[j]:
                C[j] = M[i][j]
    return C


# --------------------------------- programa principal
m = int(input("Número de filas: "))
n = int(input("Número de columnas: "))
A = leerMatriz(m, n, "A")

print("Máximos por fila:   ", maximosPorFila(A))
print("Máximos por columna:", maximosPorColumna(A))
