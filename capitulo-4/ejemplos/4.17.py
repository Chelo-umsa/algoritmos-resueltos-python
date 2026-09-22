# Ejemplo 4.17 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Leer elemento por elemento una matriz A de m filas y n columnas.
# Construir y mostrar la matriz transpuesta, de n filas y m
# columnas.

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

def transpuesta(M):
    """Devuelve la transpuesta: filas por columnas."""
    T = crearNula(len(M[0]), len(M))
    for i in range(len(M)):
        for j in range(len(M[0])):
            T[j][i] = M[i][j]
    return T


# --------------------------------- programa principal
m = int(input("Número de filas: "))
n = int(input("Número de columnas: "))
A = leerMatriz(m, n, "A")

mostrarMatriz(A, "Matriz A:")
mostrarMatriz(transpuesta(A), "Transpuesta:")
