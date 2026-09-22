# Ejemplo 2.7 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Obtener la potencia de una base B elevada a un exponente entero no
# negativo E, sin usar el operador de potencia ni el de
# multiplicación.

def potencia(B, E):
    """Devuelve B elevado a E llamando a producto."""
    P = 1
    for C in range(1, E + 1):
        P = producto(P, B)
    return P


# ------------------------ definidos en ejemplos anteriores
def producto(M, N):
    """Devuelve M por N usando sólo sumas."""
    P = 0
    for C in range(1, N + 1):
        P = P + M
    return P


# --------------------------------- programa principal
B = int(input("Ingrese la base: "))
E = int(input("Ingrese el exponente: "))
P = potencia(B, E)
print(f"La potencia es {P}")
