# Ejemplo 1.3 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# Un estudiante de la Facultad de Tecnología rinde tres parciales y
# un examen final, los cuatro con la misma ponderación. Obtener el
# promedio de sus calificaciones.

N1 = float(input("Nota del primer parcial: "))
N2 = float(input("Nota del segundo parcial: "))
N3 = float(input("Nota del tercer parcial: "))
N4 = float(input("Nota del examen final: "))
S = N1 + N2 + N3 + N4
P = S / 4
print(f"El promedio del estudiante es {P}")
