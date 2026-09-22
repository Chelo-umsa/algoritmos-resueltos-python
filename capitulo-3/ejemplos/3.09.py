# Ejemplo 3.9 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Ordenar un vector de N elementos en forma ascendente y también en
# forma descendente.

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


# --------------------------------- programa principal
N = int(input("Tamaño del vector: "))
V = leerVector(N, "V")

mostrar(V, "Vector original: ")
mostrar(ordenarAscendente(V), "Orden ascendente: ")
mostrar(ordenarDescendente(V), "Orden descendente:")
