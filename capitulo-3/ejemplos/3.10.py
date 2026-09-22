# Ejemplo 3.10 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Ingresar dos vectores A y B, que pueden ser de tamaños diferentes.
# Construir el vector C colocando los elementos de B a continuación
# de los de A. Presentar los tres vectores y luego los tres
# ordenados.

def leerVector(N, nombre):
    """Lee N elementos enteros desde el teclado."""
    V = [0] * N
    for i in range(N):
        V[i] = int(input(nombre + "[" + str(i) + "]: "))
    return V

def mostrar(V, titulo):
    """Escribe el vector precedido de un título."""
    print(titulo, V)

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

def concatenar(A, B):
    """Los elementos de A seguidos por los de B."""
    C = [0] * (len(A) + len(B))
    for i in range(len(A)):
        C[i] = A[i]
    for i in range(len(B)):
        C[len(A) + i] = B[i]
    return C


# --------------------------------- programa principal
M = int(input("Tamaño del vector A: "))
N = int(input("Tamaño del vector B: "))
A = leerVector(M, "A")
B = leerVector(N, "B")
C = concatenar(A, B)

mostrar(A, "Vector A:")
mostrar(B, "Vector B:")
mostrar(C, "Vector C:")

mostrar(ordenarAscendente(A), "A ordenado:")
mostrar(ordenarAscendente(B), "B ordenado:")
mostrar(ordenarAscendente(C), "C ordenado:")
