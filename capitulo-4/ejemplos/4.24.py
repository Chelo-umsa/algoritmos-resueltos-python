# Ejemplo 4.24 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Expresar un sistema de dos ecuaciones lineales con dos incógnitas
# en su forma matricial AX = B. Leer las matrices A y B, calcular y
# mostrar el determinante de A y, si fuera distinto de cero, usar la
# regla de Cramer para calcular y mostrar las soluciones.

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

def determinante2(A):
    """Determinante de una matriz de dos por dos."""
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]

def cramer2(A, B):
    """Devuelve x e y por la regla de Cramer.

    Supone que el determinante de A no es cero.
    """
    d = determinante2(A)
    Ax = [[B[0][0], A[0][1]], [B[1][0], A[1][1]]]
    Ay = [[A[0][0], B[0][0]], [A[1][0], B[1][0]]]
    return determinante2(Ax) / d, determinante2(Ay) / d


# --------------------------------- programa principal
print("Coeficientes del sistema")
A = leerMatriz(2, 2, "A")
print("Términos independientes")
B = leerMatriz(2, 1, "B")

mostrarMatriz(A, "Matriz A:")
d = determinante2(A)
print("Determinante de A:", d)

if d == 0:
    print("El sistema no tiene solución única")
else:
    x, y = cramer2(A, B)
    print("x =", x)
    print("y =", y)
