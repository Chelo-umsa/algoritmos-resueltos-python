# Ejemplo 4.7 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Para cualquier n natural, generar y mostrar las siete matrices de
# la figura. Las tres últimas sólo existen para n impar.

def crearNula(m, n):
    """Matriz de ceros de m filas y n columnas."""
    M = []
    for i in range(m):
        M.append([0] * n)
    return M

def mostrarMatriz(M, titulo):
    """Escribe la matriz fila por fila, con un título."""
    print("\n" + titulo)
    for i in range(len(M)):
        print(M[i])

def marco(n):
    """Inciso b: unos en el borde, ceros en el interior."""
    M = crearNula(n, n)
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                M[i][j] = 1
    return M

def antidiagonal(n):
    """Inciso d: unos en la diagonal secundaria."""
    M = crearNula(n, n)
    for i in range(n):
        for j in range(n):
            if i + j == n - 1:
                M[i][j] = 1
    return M

def triangularInferior(n):
    """Inciso e: unos bajo la diagonal principal."""
    M = crearNula(n, n)
    for i in range(n):
        for j in range(n):
            if i >= j:
                M[i][j] = 1
    return M

def sobreSecundaria(n):
    """Inciso f: unos sobre la diagonal secundaria."""
    M = crearNula(n, n)
    for i in range(n):
        for j in range(n):
            if i + j <= n - 1:
                M[i][j] = 1
    return M

def rombo(n):
    """Inciso h: rombo. Sólo para n impar."""
    M = crearNula(n, n)
    c = n // 2
    for i in range(n):
        for j in range(n):
            if abs(i - c) + abs(j - c) <= c:
                M[i][j] = 1
    return M

def reloj(n):
    """Inciso i: reloj de arena. Sólo para n impar."""
    M = crearNula(n, n)
    c = n // 2
    for i in range(n):
        for j in range(n):
            if abs(i - c) >= abs(j - c):
                M[i][j] = 1
    return M

def ventana(n):
    """Inciso j: ventana. Sólo para n impar."""
    M = crearNula(n, n)
    c = n // 2
    for i in range(n):
        for j in range(n):
            if i != c and j != c:
                M[i][j] = 1
    return M


# --------------------------------- programa principal
n = int(input("Orden de la matriz: "))

mostrarMatriz(marco(n), "b) Marco:")
mostrarMatriz(antidiagonal(n), "d) Diagonal secundaria:")
mostrarMatriz(triangularInferior(n), "e) Triángulo inf.:")
mostrarMatriz(sobreSecundaria(n), "f) Sobre la secundaria:")

if n % 2 == 0:
    print("\nLas figuras h, i y j piden orden impar")
else:
    mostrarMatriz(rombo(n), "h) Rombo:")
    mostrarMatriz(reloj(n), "i) Reloj de arena:")
    mostrarMatriz(ventana(n), "j) Ventana:")
