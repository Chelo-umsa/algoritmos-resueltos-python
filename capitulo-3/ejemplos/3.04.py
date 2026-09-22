# Ejemplo 3.4 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Efectuar el producto escalar de dos vectores A y B del mismo
# número de elementos, entendido como la suma de los productos de
# sus elementos correspondientes.

def leerVector(N, nombre):
    """Lee N elementos enteros desde el teclado."""
    V = [0] * N
    for i in range(N):
        V[i] = int(input(nombre + "[" + str(i) + "]: "))
    return V

def mostrar(V, titulo):
    """Escribe el vector precedido de un título."""
    print(titulo, V)

def productoEscalar(A, B):
    """Suma de los productos posición a posición."""
    S = 0
    for i in range(len(A)):
        S = S + A[i] * B[i]
    return S


# --------------------------------- programa principal
N = int(input("Tamaño de los vectores: "))
A = leerVector(N, "A")
B = leerVector(N, "B")

mostrar(A, "Vector A:")
mostrar(B, "Vector B:")
print("Producto escalar:", productoEscalar(A, B))
