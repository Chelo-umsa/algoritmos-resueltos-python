# Ejemplo 3.12 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Mediante un menú de opciones, permitir definir el tamaño de un
# vector, cargarlo desde el teclado o con datos aleatorios dentro de
# un intervalo, listarlo, ordenarlo en forma creciente o
# decreciente, buscar un dato, reemplazarlo y eliminarlo.

import random

def mostrar(V, titulo):
    """Escribe el vector precedido de un título."""
    print(titulo, V)

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

def cargarAleatorio(N, k, w):
    """Devuelve N elementos aleatorios entre k y w."""
    V = [0] * N
    for i in range(N):
        V[i] = random.randint(k, w)
    return V

def buscar(V, dato):
    """Devuelve la posición del dato, o -1 si no está."""
    for i in range(len(V)):
        if V[i] == dato:
            return i
    return -1

def reemplazar(V, viejo, nuevo):
    """Reemplaza la primera aparición del dato."""
    P = buscar(V, viejo)
    if P == -1:
        return False
    V[P] = nuevo
    return True

def eliminar(V, dato):
    """Devuelve un vector sin la primera aparición."""
    P = buscar(V, dato)
    if P == -1:
        return V
    W = [0] * (len(V) - 1)
    for i in range(P):
        W[i] = V[i]
    for i in range(P + 1, len(V)):
        W[i - 1] = V[i]
    return W


# --------------------------------- programa principal
V = []

opcion = ""
while opcion != "z":
    print()
    print("a) Definir tamaño     f) Ordenar decreciente")
    print("b) Cargar teclado     g) Buscar un dato")
    print("c) Cargar aleatorio   h) Reemplazar un dato")
    print("d) Listar vector      i) Eliminar un dato")
    print("e) Ordenar creciente  z) Salir")
    opcion = input("Elija una opción: ")

    if opcion == "a":
        N = int(input("Tamaño del vector: "))
        V = [0] * N
        print("Vector de", N, "posiciones creado")

    elif opcion == "b":
        N = int(input("Tamaño del vector: "))
        V = leerVector(N, "V")

    elif opcion == "c":
        N = int(input("Tamaño del vector: "))
        k = int(input("Límite inferior: "))
        w = int(input("Límite superior: "))
        if k > w:
            print("Error: el inferior supera al superior")
        else:
            V = cargarAleatorio(N, k, w)

    elif opcion != "z" and len(V) == 0:
        print("Error: primero debe cargar el vector")

    elif opcion == "d":
        mostrar(V, "Vector:")

    elif opcion == "e":
        V = ordenarAscendente(V)
        mostrar(V, "Vector:")

    elif opcion == "f":
        V = ordenarDescendente(V)
        mostrar(V, "Vector:")

    elif opcion == "g":
        dato = int(input("Dato a buscar: "))
        P = buscar(V, dato)
        if P == -1:
            print("El dato no figura en el vector")
        else:
            print("El dato está en la posición", P)

    elif opcion == "h":
        viejo = int(input("Dato a reemplazar: "))
        nuevo = int(input("Nuevo valor: "))
        if reemplazar(V, viejo, nuevo):
            mostrar(V, "Vector:")
        else:
            print("El dato no figura en el vector")

    elif opcion == "i":
        dato = int(input("Dato a eliminar: "))
        if buscar(V, dato) == -1:
            print("El dato no figura en el vector")
        else:
            V = eliminar(V, dato)
            mostrar(V, "Vector:")

print("Fin del programa")
