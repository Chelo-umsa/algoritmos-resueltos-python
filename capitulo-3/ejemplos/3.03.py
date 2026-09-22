# Ejemplo 3.3 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Leer dos vectores y mostrar su suma. Si los vectores tuvieran
# distinto tamaño, mostrar un mensaje de error.

def leerVector(N, nombre):
    """Lee N elementos enteros desde el teclado."""
    V = [0] * N
    for i in range(N):
        V[i] = int(input(nombre + "[" + str(i) + "]: "))
    return V

def mostrar(V, titulo):
    """Escribe el vector precedido de un título."""
    print(titulo, V)

def sumaVectores(A, B):
    """Devuelve el vector suma de A y B."""
    C = [0] * len(A)
    for i in range(len(A)):
        C[i] = A[i] + B[i]
    return C


# --------------------------------- programa principal
M = int(input("Tamaño del vector A: "))
N = int(input("Tamaño del vector B: "))

if M != N:
    print("Error: los vectores deben tener el mismo tamaño")
else:
    A = leerVector(M, "A")
    B = leerVector(N, "B")
    mostrar(A, "Vector A:")
    mostrar(B, "Vector B:")
    mostrar(sumaVectores(A, B), "Suma:   ")
