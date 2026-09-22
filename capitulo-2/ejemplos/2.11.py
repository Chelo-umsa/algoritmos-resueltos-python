# Ejemplo 2.11 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Calcular el número de combinaciones que se obtienen al agrupar N
# elementos de M en M, sabiendo que ese número es N! dividido entre
# el producto de M! y (N − M)!. Debe cumplirse que M esté entre 0 y
# N.

# ------------------------ definidos en ejemplos anteriores
def factorial(D):
    """Devuelve el factorial de D."""
    F = 1
    for C in range(1, D + 1):
        F = F * C
    return F


# --------------------------------- programa principal
N = int(input("Ingrese la cantidad de elementos: "))
M = int(input("Ingrese el tamaño de cada grupo: "))
if M > N or M < 0:
    print("Error: el grupo debe estar entre 0 y N")
else:
    R = factorial(N) // (factorial(M) * factorial(N - M))
    print(f"La cantidad de combinaciones es {R}")
