# Ejemplo 4.21 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Una matriz contiene la producción en toneladas de cinco minerales
# durante los seis meses de un semestre. Dos vectores contienen los
# nombres de los minerales y los de los meses. Dado un mineral,
# determinar en qué mes o meses ocurrió su mayor producción, y
# determinar también el mineral o los minerales de menor producción
# en todo el semestre.

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

def totalesPorFila(M):
    """Devuelve un vector con la suma de cada fila."""
    F = [0] * len(M)
    for i in range(len(M)):
        S = 0
        for j in range(len(M[i])):
            S = S + M[i][j]
        F[i] = S
    return F


# --------------------------------- programa principal
minerales = ["Estaño", "Zinc", "Plata", "Plomo", "Antimonio"]
meses = ["Enero", "Febrero", "Marzo",
         "Abril", "Mayo", "Junio"]

A = leerMatriz(len(minerales), len(meses), "Produccion")

k = int(input("Mineral a consultar, de 1 a 5: "))
fila = A[k - 1]
mejor = mayorVector(fila)
for j in range(len(meses)):
    if fila[j] == mejor:
        print("Mayor producción en", meses[j], "con", mejor)

T = totalesPorFila(A)
peor = menorVector(T)
for i in range(len(minerales)):
    if T[i] == peor:
        print("Menor producción semestral:", minerales[i])
