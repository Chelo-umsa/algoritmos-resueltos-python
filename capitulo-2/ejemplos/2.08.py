# Ejemplo 2.8 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Obtener el factorial de un número empleando únicamente sumas, sin
# usar el operador de multiplicación.

def factorialSumas(N):
    """Devuelve el factorial de N llamando a producto."""
    F = 1
    for C in range(2, N + 1):
        F = producto(F, C)
    return F


# ------------------------ definidos en ejemplos anteriores
def producto(M, N):
    """Devuelve M por N usando sólo sumas."""
    P = 0
    for C in range(1, N + 1):
        P = P + M
    return P


# --------------------------------- programa principal
N = int(input("Ingrese un número: "))
F = factorialSumas(N)
print(f"El factorial es {F}")
