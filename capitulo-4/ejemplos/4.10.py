# Ejemplo 4.10 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Ingresar una matriz de m filas y n columnas y un número p
# comprendido entre 1 y m. Mostrar el valor máximo de la fila p.

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

def maximoFila(M, p):
    """Mayor elemento de la fila cuyo índice es p."""
    return mayorVector(M[p])


# --------------------------------- programa principal
m = int(input("Número de filas: "))
n = int(input("Número de columnas: "))
A = leerMatriz(m, n, "A")
p = int(input("Fila que desea consultar, de 1 a %d: " % m))

if p < 1 or p > m:
    print("Error: esa fila no existe")
else:
    print("Máximo de la fila", p, "es", maximoFila(A, p - 1))
