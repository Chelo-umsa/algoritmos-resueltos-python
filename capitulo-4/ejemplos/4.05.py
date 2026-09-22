# Ejemplo 4.5 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Generar y mostrar la matriz Tn, que tiene el número de columna en
# las posiciones ubicadas debajo de la diagonal secundaria y un uno
# en las demás.

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

def escalonada(n):
    """Tn: número de columna bajo la diagonal secundaria."""
    M = crearNula(n, n)
    for i in range(n):
        for j in range(n):
            if i + j >= n:
                M[i][j] = j + 1
            else:
                M[i][j] = 1
    return M


# --------------------------------- programa principal
n = int(input("Orden de la matriz: "))

mostrarMatriz(escalonada(n), "Matriz Tn:")
