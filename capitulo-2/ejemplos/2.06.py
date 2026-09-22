# Ejemplo 2.6 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Obtener el producto de dos números enteros empleando únicamente
# sumas, es decir, sin usar el operador de multiplicación. El
# multiplicador debe ser no negativo.

def producto(M, N):
    """Devuelve M por N usando sólo sumas."""
    P = 0
    for C in range(1, N + 1):
        P = P + M
    return P


# --------------------------------- programa principal
M = int(input("Ingrese el multiplicando: "))
N = int(input("Ingrese el multiplicador: "))
P = producto(M, N)
print(f"El producto es {P}")
