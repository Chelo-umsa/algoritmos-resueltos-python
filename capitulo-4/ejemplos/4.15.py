# Ejemplo 4.15 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Sumar dos matrices, si fueran del mismo tamaño. En caso contrario,
# mostrar un mensaje de error.

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

def sumaMatrices(A, B):
    """Devuelve la suma de dos matrices del mismo tamaño."""
    C = crearNula(len(A), len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] + B[i][j]
    return C


# --------------------------------- programa principal
m = int(input("Filas de A: "))
n = int(input("Columnas de A: "))
p = int(input("Filas de B: "))
q = int(input("Columnas de B: "))

if m != p or n != q:
    print("Error: las matrices deben tener igual tamaño")
else:
    A = leerMatriz(m, n, "A")
    B = leerMatriz(p, q, "B")
    mostrarMatriz(A, "Matriz A:")
    mostrarMatriz(B, "Matriz B:")
    mostrarMatriz(sumaMatrices(A, B), "Suma:")
