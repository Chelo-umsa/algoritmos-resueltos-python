# Propuesto 4.30 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Determinar si una matriz cuadrada de orden n es un cuadrado mágico
# en sentido estricto: además de que filas, columnas y diagonales
# sumen lo mismo, sus elementos deben ser los números del 1 al n²
# sin repetir.

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

def copiar(V):
    """Devuelve un vector nuevo igual a V."""
    W = [0] * len(V)
    for i in range(len(V)):
        W[i] = V[i]
    return W

def ordenarAscendente(V):
    """Copia de V ordenada de menor a mayor."""
    W = copiar(V)
    for i in range(len(W) - 1):
        for j in range(i + 1, len(W)):
            if W[j] < W[i]:
                S = W[i]
                W[i] = W[j]
                W[j] = S
    return W

def sumasIguales(M):
    """Verdadero si filas, columnas y diagonales suman igual."""
    n = len(M)
    objetivo = 0
    for j in range(n):
        objetivo = objetivo + M[0][j]
    P = 0
    S = 0
    for i in range(n):
        F = 0
        C = 0
        for j in range(n):
            F = F + M[i][j]
            C = C + M[j][i]
        if F != objetivo or C != objetivo:
            return False
        P = P + M[i][i]
        S = S + M[i][n - 1 - i]
    return P == objetivo and S == objetivo

def usaDel1alN2(M):
    """Verdadero si los elementos son 1, 2, ..., n al cuadrado."""
    n = len(M)
    V = [0] * (n * n)
    for i in range(n):
        for j in range(n):
            V[i * n + j] = M[i][j]
    V = ordenarAscendente(V)
    for k in range(n * n):
        if V[k] != k + 1:
            return False
    return True


# --------------------------------- programa principal
n = int(input("Orden de la matriz: "))
A = leerMatriz(n, n, "A")
if usaDel1alN2(A) and sumasIguales(A):
    print("Es un cuadrado mágico")
else:
    print("No es un cuadrado mágico")
