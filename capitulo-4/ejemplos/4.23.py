# Ejemplo 4.23 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Se dice que una matriz tiene un punto de silla si alguna de sus
# posiciones contiene a la vez el menor valor de su fila y el mayor
# de su columna. Ingresar una matriz de números enteros y calcular
# la posición de un punto de silla, si es que existe.

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

def menorVector(V):
    """Devuelve el menor elemento de un vector no vacío."""
    m = V[0]
    for i in range(1, len(V)):
        if V[i] < m:
            m = V[i]
    return m

def puntoDeSilla(M):
    """Devuelve la fila y la columna del punto de silla.

    Es el menor de su fila y el mayor de su columna.
    Si no existe devuelve -1 y -1.
    """
    for i in range(len(M)):
        menor = menorVector(M[i])
        for j in range(len(M[i])):
            if M[i][j] == menor:
                mayor = M[0][j]
                for k in range(1, len(M)):
                    if M[k][j] > mayor:
                        mayor = M[k][j]
                if M[i][j] == mayor:
                    return i, j
    return -1, -1


# --------------------------------- programa principal
m = int(input("Número de filas: "))
n = int(input("Número de columnas: "))
A = leerMatriz(m, n, "A")

mostrarMatriz(A, "Matriz A:")
f, c = puntoDeSilla(A)
if f == -1:
    print("La matriz no tiene punto de silla")
else:
    print("Punto de silla en la fila", f, "y la columna", c)
    print("Su valor es", A[f][c])
