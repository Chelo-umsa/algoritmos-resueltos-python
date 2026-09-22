# Ejemplo 4.8 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Generar y mostrar la matriz espiral de orden n, numerada de uno en
# uno desde el ángulo superior izquierdo y avanzando en el sentido
# de las agujas del reloj hacia el centro.

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

def espiral(n):
    """Matriz espiral desde el ángulo superior izquierdo."""
    M = crearNula(n, n)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    i = 0
    j = 0
    d = 0
    for k in range(1, n * n + 1):
        M[i][j] = k
        pi = i + di[d]
        pj = j + dj[d]
        fuera = pi < 0 or pi >= n or pj < 0 or pj >= n
        if fuera or M[pi][pj] != 0:
            d = (d + 1) % 4
            pi = i + di[d]
            pj = j + dj[d]
        i = pi
        j = pj
    return M


# --------------------------------- programa principal
n = int(input("Orden de la matriz: "))

mostrarMatriz(espiral(n), "Matriz espiral:")
