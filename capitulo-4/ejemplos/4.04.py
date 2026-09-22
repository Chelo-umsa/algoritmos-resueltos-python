# Ejemplo 4.4 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Generar y mostrar la matriz mariposa de orden n, con unos sobre
# sus dos diagonales y ceros en el resto.

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

def mariposa(n):
    """Matriz mariposa: unos en las dos diagonales."""
    M = crearNula(n, n)
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                M[i][j] = 1
    return M


# --------------------------------- programa principal
n = int(input("Orden de la matriz: "))

mostrarMatriz(mariposa(n), "Matriz mariposa:")
