# Propuesto 3.15 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Leer dos vectores A y B del mismo tamaño. Ordenar A en forma
# ascendente y B en forma descendente, construir el vector C con los
# productos de los elementos correspondientes y mostrar C ordenado
# en forma ascendente.

def leerVector(N, nombre):
    """Lee N elementos enteros desde el teclado."""
    V = [0] * N
    for i in range(N):
        V[i] = int(input(nombre + "[" + str(i) + "]: "))
    return V

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

def ordenarDescendente(V):
    """Copia de V ordenada de mayor a menor."""
    W = copiar(V)
    for i in range(len(W) - 1):
        for j in range(i + 1, len(W)):
            if W[j] > W[i]:
                S = W[i]
                W[i] = W[j]
                W[j] = S
    return W

def productos(A, B):
    """Vector de los productos posición a posición."""
    C = [0] * len(A)
    for i in range(len(A)):
        C[i] = A[i] * B[i]
    return C


# --------------------------------- programa principal
N = int(input("Tamaño de los vectores: "))
A = ordenarAscendente(leerVector(N, "A"))
B = ordenarDescendente(leerVector(N, "B"))
C = ordenarAscendente(productos(A, B))
print("A:", A)
print("B:", B)
print("C:", C)
