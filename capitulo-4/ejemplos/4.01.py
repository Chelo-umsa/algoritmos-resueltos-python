# Ejemplo 4.1 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Generar y mostrar la matriz nula O de tamaño m × n, es decir,
# aquella cuyos elementos son todos iguales a cero.

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

# --------------------------------- programa principal
m = int(input("Número de filas: "))
n = int(input("Número de columnas: "))

mostrarMatriz(crearNula(m, n), "Matriz nula:")
