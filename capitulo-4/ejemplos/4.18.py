# Ejemplo 4.18 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Una matriz cuadrada se denomina simétrica si coincide con su
# transpuesta. Determinar si una matriz dada es simétrica.

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

def transpuesta(M):
    """Devuelve la transpuesta: filas por columnas."""
    T = crearNula(len(M[0]), len(M))
    for i in range(len(M)):
        for j in range(len(M[0])):
            T[j][i] = M[i][j]
    return T

def esSimetrica(M):
    """Verdadero si la matriz coincide con su transpuesta."""
    T = transpuesta(M)
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] != T[i][j]:
                return False
    return True


# --------------------------------- programa principal
n = int(input("Orden de la matriz: "))
A = leerMatriz(n, n, "A")

mostrarMatriz(A, "Matriz A:")
if esSimetrica(A):
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")
