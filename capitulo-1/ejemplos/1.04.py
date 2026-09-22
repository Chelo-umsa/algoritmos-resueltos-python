# Ejemplo 1.4 — Algoritmos resueltos con Python
# J. M. Flores Monrroy
#
# En el circuito de una sola malla de la figura, una fuente de
# tensión V alimenta una resistencia R por la que circula una
# corriente I. Calcular la potencia eléctrica que disipa el
# circuito, sabiendo que P = I × V.

I = float(input("Corriente en amperios: "))
V = float(input("Tensión en voltios: "))
P = I * V
print(f"La potencia del circuito es {P}")
