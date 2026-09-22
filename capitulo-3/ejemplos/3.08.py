# Ejemplo 3.8 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dado un vector V de N elementos, construir y presentar el vector W
# formado con los elementos de V en orden invertido. Por ejemplo, si
# V es 1, 5, 2, 2, 7, 3 entonces W es 3, 7, 2, 2, 5, 1.

def leerVector(N, nombre):
    """Lee N elementos enteros desde el teclado."""
    V = [0] * N
    for i in range(N):
        V[i] = int(input(nombre + "[" + str(i) + "]: "))
    return V

def mostrar(V, titulo):
    """Escribe el vector precedido de un título."""
    print(titulo, V)

def invertirVector(V):
    """Devuelve un vector nuevo con V en orden inverso."""
    W = [0] * len(V)
    for i in range(len(V)):
        W[i] = V[len(V) - 1 - i]
    return W


# --------------------------------- programa principal
N = int(input("Tamaño del vector: "))
V = leerVector(N, "V")

mostrar(V, "Vector V:")
mostrar(invertirVector(V), "Vector W:")
