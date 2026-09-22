# Propuesto 4.29 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Resolver un sistema de tres ecuaciones lineales con tres
# incógnitas por la regla de Cramer, calculando antes el
# determinante de la matriz de coeficientes.

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

def determinante3(A):
    """Determinante de una matriz de tres por tres."""
    a = A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
    b = A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
    c = A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    return a - b + c

def reemplazarColumna(A, B, c):
    """Copia de A con la columna c sustituida por B."""
    R = crearNula(3, 3)
    for i in range(3):
        for j in range(3):
            if j == c:
                R[i][j] = B[i][0]
            else:
                R[i][j] = A[i][j]
    return R


# --------------------------------- programa principal
print("Coeficientes del sistema")
A = leerMatriz(3, 3, "A")
print("Términos independientes")
B = leerMatriz(3, 1, "B")
d = determinante3(A)
print("Determinante de A:", d)
if d == 0:
    print("El sistema no tiene solución única")
else:
    for c in range(3):
        v = determinante3(reemplazarColumna(A, B, c)) / d
        print("xyz"[c], "=", v)
