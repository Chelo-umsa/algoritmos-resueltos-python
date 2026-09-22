# Ejemplo 3.2 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Dado un vector de N elementos enteros, calcular y mostrar: la suma
# de los dos últimos elementos, el mayor sin ordenar el vector, la
# suma de los dos mayores, la suma de los elementos, la suma de sus
# cuadrados, el promedio de los positivos pares, el promedio de los
# elementos de lugar par, si hay más pares positivos que impares
# positivos, si hay más positivos que negativos, el porcentaje de
# pares positivos y de impares negativos, la posición del primer
# múltiplo de 3, el promedio entre el mínimo y el máximo, la
# cantidad de positivos primos y cuántas veces figura un valor K.

def leerVector(N, nombre):
    """Lee N elementos enteros desde el teclado."""
    V = [0] * N
    for i in range(N):
        V[i] = int(input(nombre + "[" + str(i) + "]: "))
    return V

def sumaDosUltimos(V):
    """Devuelve la suma de los dos últimos elementos."""
    return V[len(V) - 1] + V[len(V) - 2]

def mayor(V):
    """Devuelve el mayor, sin ordenar el vector."""
    M = V[0]
    for i in range(1, len(V)):
        if V[i] > M:
            M = V[i]
    return M

def sumaDosMayores(V):
    """Suma de los dos elementos de mayor valor."""
    if V[0] > V[1]:
        M1 = V[0]
        M2 = V[1]
    else:
        M1 = V[1]
        M2 = V[0]
    for i in range(2, len(V)):
        if V[i] > M1:
            M2 = M1
            M1 = V[i]
        elif V[i] > M2:
            M2 = V[i]
    return M1 + M2

def suma(V):
    """Devuelve la suma de todos los elementos."""
    S = 0
    for i in range(len(V)):
        S = S + V[i]
    return S

def sumaCuadrados(V):
    """Suma de los cuadrados de los elementos."""
    S = 0
    for i in range(len(V)):
        S = S + V[i] * V[i]
    return S

def promedioParesPositivos(V):
    """Promedio de los pares positivos, o None."""
    S = 0
    Q = 0
    for i in range(len(V)):
        if V[i] > 0 and V[i] % 2 == 0:
            S = S + V[i]
            Q = Q + 1
    if Q == 0:
        return None
    return S / Q

def promedioLugaresPares(V):
    """Promedio de los elementos de posición par."""
    S = 0
    Q = 0
    for i in range(0, len(V), 2):
        S = S + V[i]
        Q = Q + 1
    return S / Q

def cuentaParesImparesPositivos(V):
    """Cuántos positivos son pares y cuántos impares."""
    P = 0
    I = 0
    for i in range(len(V)):
        if V[i] > 0:
            if V[i] % 2 == 0:
                P = P + 1
            else:
                I = I + 1
    return P, I

def cuentaPositivosNegativos(V):
    """Cuántos positivos y cuántos negativos hay."""
    P = 0
    N = 0
    for i in range(len(V)):
        if V[i] > 0:
            P = P + 1
        elif V[i] < 0:
            N = N + 1
    return P, N

def porcentajes(V):
    """Porcentaje de pares positivos e impares negativos."""
    PP = 0
    IN = 0
    for i in range(len(V)):
        if V[i] > 0 and V[i] % 2 == 0:
            PP = PP + 1
        if V[i] < 0 and V[i] % 2 != 0:
            IN = IN + 1
    return PP * 100 / len(V), IN * 100 / len(V)

def posicionMultiploDe3(V):
    """Posición del primer múltiplo de 3, o -1."""
    for i in range(len(V)):
        if V[i] % 3 == 0:
            return i
    return -1

def promedioMinMax(V):
    """Promedio entre el menor y el mayor elemento."""
    m = V[0]
    M = V[0]
    for i in range(1, len(V)):
        if V[i] < m:
            m = V[i]
        if V[i] > M:
            M = V[i]
    return (m + M) / 2

def cantidadPrimosPositivos(V):
    """Cuántos elementos positivos son primos."""
    Q = 0
    for i in range(len(V)):
        if V[i] > 0 and esPrimo(V[i]):
            Q = Q + 1
    return Q

def vecesQueAparece(V, K):
    """Cuántas veces figura el valor K en el vector."""
    Q = 0
    for i in range(len(V)):
        if V[i] == K:
            Q = Q + 1
    return Q


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
V = leerVector(N, "V")
K = int(input("Valor a buscar: "))

print("a) Suma dos últimos:", sumaDosUltimos(V))
print("b) Mayor elemento:", mayor(V))
print("c) Suma dos mayores:", sumaDosMayores(V))
print("d) Suma de los elementos:", suma(V))
print("e) Suma de los cuadrados:", sumaCuadrados(V))

P = promedioParesPositivos(V)
if P is None:
    print("f) No hay elementos pares positivos")
else:
    print("f) Promedio pares positivos:", P)

print("g) Promedio lugares pares:", promedioLugaresPares(V))

PA, IM = cuentaParesImparesPositivos(V)
if PA > IM:
    print("h) Hay más pares positivos")
elif IM > PA:
    print("h) Hay más impares positivos")
else:
    print("h) Hay la misma cantidad")

PO, NE = cuentaPositivosNegativos(V)
if PO > NE:
    print("i) Hay más positivos")
elif NE > PO:
    print("i) Hay más negativos")
else:
    print("i) Hay la misma cantidad")

PP, IN = porcentajes(V)
print("j) Pares pos:", PP, "%  Impares neg:", IN, "%")

POS = posicionMultiploDe3(V)
if POS == -1:
    print("k) No hay múltiplos de 3")
else:
    print("k) Primer múltiplo de 3 en", POS)

print("l) Promedio mín y máx:", promedioMinMax(V))
print("m) Positivos primos:", cantidadPrimosPositivos(V))
print("n) El valor", K, "figura", vecesQueAparece(V, K))
