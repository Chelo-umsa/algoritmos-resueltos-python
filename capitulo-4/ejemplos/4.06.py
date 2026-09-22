# Ejemplo 4.6 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Generar y mostrar la matriz Qn, en la que cada elemento es el
# producto del número de su fila por el de su columna.

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

def tablaProductos(n):
    """Devuelve Qn: número de fila por número de columna."""
    M = crearNula(n, n)
    for i in range(n):
        for j in range(n):
            M[i][j] = (i + 1) * (j + 1)
    return M


# --------------------------------- programa principal
n = int(input("Orden de la matriz: "))

mostrarMatriz(tablaProductos(n), "Matriz Qn:")
