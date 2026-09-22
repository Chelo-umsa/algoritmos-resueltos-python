# Ejemplo 3.11 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Las estaturas de los estudiantes de un curso se almacenan en un
# vector. Mostrar las estaturas de los tres estudiantes más altos.

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
N = int(input("Cantidad de estudiantes: "))
V = leerVector(N, "Estatura")

mostrar(V, "Estaturas:")

if N < 3:
    print("Error: se necesitan al menos tres estudiantes")
else:
    W = ordenarDescendente(V)
    print("Las tres más altas:", W[0], W[1], W[2])
