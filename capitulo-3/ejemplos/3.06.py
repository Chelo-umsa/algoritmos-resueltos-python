# Ejemplo 3.6 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Las notas finales sobre 100 de los estudiantes de un curso se
# almacenan en un vector. Mostrar el vector, el porcentaje de
# aprobados y de reprobados sabiendo que la nota mínima de
# aprobación es 51, y la cantidad de estudiantes con nota inferior
# al promedio del curso.

def leerVector(N, nombre):
    """Lee N elementos enteros desde el teclado."""
    V = [0] * N
    for i in range(N):
        V[i] = int(input(nombre + "[" + str(i) + "]: "))
    return V

def mostrar(V, titulo):
    """Escribe el vector precedido de un título."""
    print(titulo, V)

def suma(V):
    """Devuelve la suma de todos los elementos."""
    S = 0
    for i in range(len(V)):
        S = S + V[i]
    return S

def promedio(V):
    """Devuelve el promedio de los elementos."""
    return suma(V) / len(V)

def contarAprobados(V, minima):
    """Cuántos elementos alcanzan la nota mínima."""
    Q = 0
    for i in range(len(V)):
        if V[i] >= minima:
            Q = Q + 1
    return Q

def contarMenoresA(V, valor):
    """Cuántos elementos son menores que el valor."""
    Q = 0
    for i in range(len(V)):
        if V[i] < valor:
            Q = Q + 1
    return Q


# --------------------------------- programa principal
N = int(input("Cantidad de estudiantes: "))
V = leerVector(N, "Nota")

mostrar(V, "Notas del curso:")

A = contarAprobados(V, 51)
print("Porcentaje de aprobados:", A * 100 / N, "%")
print("Porcentaje de reprobados:", (N - A) * 100 / N, "%")

M = promedio(V)
print("Promedio del curso:", M)
print("Bajo el promedio:", contarMenoresA(V, M))
