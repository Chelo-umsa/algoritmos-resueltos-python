# Ejemplo 4.20 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Una matriz contiene las notas de diez alumnos en cuatro exámenes.
# Determinar el promedio de cada examen, produciendo un vector de
# cuatro elementos, e indicar la mayor nota con el número de
# estudiante y el examen en que se produjo. Si hubiera varias notas
# iguales a la mayor, indicar la última encontrada.

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

def maximoMatriz(M):
    """Devuelve el mayor elemento y su fila y columna.

    Si hay varios máximos informa el último encontrado.
    """
    V = M[0][0]
    f = 0
    c = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] >= V:
                V = M[i][j]
                f = i
                c = j
    return V, f, c

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
ALUMNOS = 10
EXAMENES = 4

A = leerMatriz(ALUMNOS, EXAMENES, "Nota")

print("Promedio por examen:")
print(promediosDe(totalesPorColumna(A), ALUMNOS))

V, f, c = maximoMatriz(A)
print("La mayor nota es", V)
print("La obtuvo el alumno", f + 1, "en el examen", c + 1)
