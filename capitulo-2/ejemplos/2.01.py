# Ejemplo 2.1 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Verificar si un número natural positivo N es fuerte, es decir, si
# la suma de los factoriales de sus dígitos es igual al número. Por
# ejemplo, 145 es fuerte porque 1! + 4! + 5! = 145.

def factorial(D):
    """Devuelve el factorial de D."""
    F = 1
    for C in range(1, D + 1):
        F = F * C
    return F

def sumaFactDigitos(N):
    """Suma los factoriales de los dígitos de N."""
    T = N
    S = 0
    while T > 0:
        D = T % 10
        S = S + factorial(D)
        T = T // 10
    return S


# --------------------------------- programa principal
N = int(input("Ingrese un número natural: "))
S = sumaFactDigitos(N)
if S == N:
    print("Es un número fuerte")
else:
    print("No es un número fuerte")
