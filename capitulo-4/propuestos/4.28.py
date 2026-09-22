# Propuesto 4.28 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Una matriz cuadrada es antisimétrica si al sumarla con su
# transpuesta se obtiene la matriz nula. Determinar si una matriz
# dada es antisimétrica.

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

def transpuesta(M):
    """Devuelve la transpuesta: filas por columnas."""
    T = crearNula(len(M[0]), len(M))
    for i in range(len(M)):
        for j in range(len(M[0])):
            T[j][i] = M[i][j]
    return T

def esAntisimetrica(M):
    """Verdadero si M más su transpuesta da la matriz nula."""
    T = transpuesta(M)
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] + T[i][j] != 0:
                return False
    return True


# --------------------------------- programa principal
n = int(input("Orden de la matriz: "))
A = leerMatriz(n, n, "A")
if esAntisimetrica(A):
    print("Es antisimétrica")
else:
    print("No es antisimétrica")
