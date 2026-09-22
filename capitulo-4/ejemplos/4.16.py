# Ejemplo 4.16 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Leer elemento por elemento las matrices A de p × q y B de m × n.
# Determinar si existe el producto AB, cosa que ocurre sólo si q es
# igual a m, y en ese caso calcular y presentar la matriz C = AB.

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
p = int(input("Filas de A: "))
q = int(input("Columnas de A: "))
m = int(input("Filas de B: "))
n = int(input("Columnas de B: "))

if q != m:
    print("Error: columnas de A y filas de B difieren")
else:
    A = leerMatriz(p, q, "A")
    B = leerMatriz(m, n, "B")
    mostrarMatriz(A, "Matriz A:")
    mostrarMatriz(B, "Matriz B:")
    mostrarMatriz(productoMatrices(A, B), "Producto C = AB:")
