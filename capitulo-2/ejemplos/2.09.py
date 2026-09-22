# Ejemplo 2.9 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Obtener la sumatoria de los factoriales de los primeros N
# elementos de la secuencia de Fibonacci. Por ejemplo, para N = 6
# los términos son 0, 1, 1, 2, 3 y 5, y la sumatoria de sus
# factoriales da 131.

def fibonacci(P):
    """Devuelve el término de la posición P."""
    A = 0
    B = 1
    for C in range(1, P):
        S = A + B
        A = B
        B = S
    return A


# ------------------------ definidos en ejemplos anteriores
def factorial(D):
    """Devuelve el factorial de D."""
    F = 1
    for C in range(1, D + 1):
        F = F * C
    return F


# --------------------------------- programa principal
N = int(input("Ingrese la cantidad de términos: "))
S = 0
for C in range(1, N + 1):
    S = S + factorial(fibonacci(C))
print(f"La sumatoria es {S}")
