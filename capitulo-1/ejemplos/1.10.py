# Ejemplo 1.10 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Leer números hasta que aparezca uno par. Considerando únicamente
# los números impares leídos, mostrar la suma de los menores a 50,
# el producto de los mayores a 100 y la cantidad de los restantes.

S = 0
P = 1
Q = 0
N = int(input("Ingrese un número: "))
while N % 2 == 1:
    if N < 50:
        S = S + N
    else:
        if N > 100:
            P = P * N
        else:
            Q = Q + 1
    N = int(input("Ingrese un número: "))
print(f"Suma de los menores a 50: {S}")
print(f"Producto de los mayores a 100: {P}")
print(f"Cantidad de los demás: {Q}")
