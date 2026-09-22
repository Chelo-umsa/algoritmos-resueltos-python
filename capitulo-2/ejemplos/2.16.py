# Ejemplo 2.16 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Leer un número de varios dígitos y mostrar el número invertido, y
# luego el mismo número perdiendo en cada línea su dígito más a la
# izquierda. Para N = 85329 las líneas son 92358, 2358, 358, 58 y 5.

def sinPrimerDigito(X):
    """Devuelve X sin su primer dígito."""
    P = 1
    T = X
    while T >= 10:
        P = P * 10
        T = T // 10
    return X % P


# ------------------------ definidos en ejemplos anteriores
def invertir(N):
    """Devuelve N con sus dígitos invertidos."""
    T = N
    R = 0
    while T > 0:
        D = T % 10
        R = R * 10 + D
        T = T // 10
    return R


# --------------------------------- programa principal
N = int(input("Ingrese un número de varios dígitos: "))
R = invertir(N)
while R > 0:
    print(R)
    R = sinPrimerDigito(R)
