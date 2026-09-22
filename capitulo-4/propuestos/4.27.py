# Propuesto 4.27 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Ingresar una matriz cuadrada A y calcular A², empleando el
# producto de matrices del ejemplo 4.16.

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

def leerMatriz(m, n, nombre):
    """Lee una matriz de m filas y n columnas."""
    M = crearNula(m, n)
    for i in range(m):
        for j in range(n):
            p = nombre + "[" + str(i) + "][" + str(j) + "]: "
            M[i][j] = int(input(p))
    return M

def productoMatrices(A, B):
    """Devuelve A por B, si las dimensiones encajan."""
    m = len(A)
    q = len(A[0])
    n = len(B[0])
    C = crearNula(m, n)
    for i in range(m):
        for j in range(n):
            S = 0
            for k in range(q):
                S = S + A[i][k] * B[k][j]
            C[i][j] = S
    return C


# --------------------------------- programa principal
n = int(input("Orden de la matriz: "))
A = leerMatriz(n, n, "A")
mostrarMatriz(productoMatrices(A, A), "A al cuadrado:")
