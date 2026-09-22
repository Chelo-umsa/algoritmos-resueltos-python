# Ejemplo 3.1 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Generar y mostrar un vector de N elementos según distintas leyes
# de formación: los naturales, los pares, los cuadrados perfectos,
# los primos, la secuencia 1, 2, 4, 7, 11, 16, la secuencia 1, 0, 2,
# 0, 3, 0 y los naturales en orden descendente.

def mostrar(V, titulo):
    """Escribe el vector precedido de un título."""
    print(titulo, V)

def vectorNatural(N):
    """Devuelve [1, 2, 3, ..., N]."""
    V = [0] * N
    for i in range(N):
        V[i] = i + 1
    return V

def vectorPares(N):
    """Devuelve [2, 4, 6, ..., 2N]."""
    V = [0] * N
    for i in range(N):
        V[i] = (i + 1) * 2
    return V

def vectorCuadrados(N):
    """Devuelve [1, 4, 9, ..., N al cuadrado]."""
    V = [0] * N
    for i in range(N):
        V[i] = (i + 1) * (i + 1)
    return V

def vectorPrimos(N):
    """Devuelve los primeros N números primos."""
    V = [0] * N
    Q = 0
    K = 1
    while Q < N:
        K = K + 1
        if esPrimo(K):
            V[Q] = K
            Q = Q + 1
    return V

def vectorAcumulado(N):
    """Devuelve [1, 2, 4, 7, 11, ...]."""
    V = [0] * N
    V[0] = 1
    for i in range(1, N):
        V[i] = V[i - 1] + i
    return V

def vectorAlternado(N):
    """Devuelve [1, 0, 2, 0, 3, 0, ...]."""
    V = [0] * N
    for i in range(N):
        if i % 2 == 0:
            V[i] = i // 2 + 1
    return V

def vectorDescendente(N):
    """Devuelve [N, N-1, ..., 2, 1]."""
    V = [0] * N
    for i in range(N):
        V[i] = N - i
    return V


# ------------------- reutilizado del ejemplo 2.2
def esPrimo(X):
    """Verdadero si X tiene dos divisores."""
    Q = 0
    for C in range(1, X + 1):
        if X % C == 0:
            Q = Q + 1
    return Q == 2


# --------------------------------- programa principal
N = int(input("Tamaño del vector: "))

mostrar(vectorNatural(N), "a) Naturales:   ")
mostrar(vectorPares(N), "b) Pares:       ")
mostrar(vectorCuadrados(N), "c) Cuadrados:   ")
mostrar(vectorPrimos(N), "d) Primos:      ")
mostrar(vectorAcumulado(N), "e) Acumulado:   ")
mostrar(vectorAlternado(N), "f) Alternado:   ")
mostrar(vectorDescendente(N), "g) Descendente: ")
