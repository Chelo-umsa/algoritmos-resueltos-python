# Ejemplo 4.19 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# En un congreso de seis días se dictan conferencias en cuatro
# salas. Con los asistentes de cada sala en cada día, obtener el
# total de congresistas por sala, el total por día, la media de
# asistencia por sala y la media diaria.

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

def totalesPorFila(M):
    """Devuelve un vector con la suma de cada fila."""
    F = [0] * len(M)
    for i in range(len(M)):
        S = 0
        for j in range(len(M[i])):
            S = S + M[i][j]
        F[i] = S
    return F

def totalesPorColumna(M):
    """Devuelve un vector con la suma de cada columna."""
    n = len(M[0])
    C = [0] * n
    for j in range(n):
        S = 0
        for i in range(len(M)):
            S = S + M[i][j]
        C[j] = S
    return C

def promediosDe(T, cantidad):
    """Divide cada total entre la cantidad indicada."""
    P = [0.0] * len(T)
    for i in range(len(T)):
        P[i] = T[i] / cantidad
    return P


# --------------------------------- programa principal
DIAS = 6
SALAS = 4

A = leerMatriz(DIAS, SALAS, "Asistentes")

porDia = totalesPorFila(A)
porSala = totalesPorColumna(A)

print("Total por día: ", porDia)
print("Total por sala:", porSala)
print("Media diaria:  ", promediosDe(porDia, SALAS))
print("Media por sala:", promediosDe(porSala, DIAS))
