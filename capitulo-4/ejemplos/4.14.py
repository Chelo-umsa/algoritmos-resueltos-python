# Ejemplo 4.14 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Tomando como base el ejercicio anterior, determinar si el máximo
# de los mínimos por columnas de una matriz es igual, mayor o menor
# que el mínimo de los máximos por filas.

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

def mayorVector(V):
    """Devuelve el mayor elemento de un vector no vacío."""
    M = V[0]
    for i in range(1, len(V)):
        if V[i] > M:
            M = V[i]
    return M

def menorVector(V):
    """Devuelve el menor elemento de un vector no vacío."""
    m = V[0]
    for i in range(1, len(V)):
        if V[i] < m:
            m = V[i]
    return m

def maximosPorFila(M):
    """Devuelve un vector con el mayor de cada fila."""
    F = [0] * len(M)
    for i in range(len(M)):
        F[i] = mayorVector(M[i])
    return F

def minimosPorColumna(M):
    """Devuelve un vector con el menor de cada columna."""
    n = len(M[0])
    C = [0] * n
    for j in range(n):
        C[j] = M[0][j]
        for i in range(1, len(M)):
            if M[i][j] < C[j]:
                C[j] = M[i][j]
    return C


# --------------------------------- programa principal
m = int(input("Número de filas: "))
n = int(input("Número de columnas: "))
A = leerMatriz(m, n, "A")

maximin = mayorVector(minimosPorColumna(A))
minimax = menorVector(maximosPorFila(A))

print("Máximo de los mínimos:", maximin)
print("Mínimo de los máximos:", minimax)
if maximin == minimax:
    print("Son iguales")
elif maximin > minimax:
    print("El máximo de los mínimos es mayor")
else:
    print("El máximo de los mínimos es menor")
