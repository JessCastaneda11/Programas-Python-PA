# p021-distancia-entre-puntos

# Crea un programa que calcule la distancia entre dos puntos en un plano cartesiano.
# El programa debe pedir al usuario que ingrese las coordenadas (x,y) del punto A
# y las coordenadas (x,y) del punto B. Utiliza la siguiente fórmula para calcular la distancia:
# d = √(ax - bx)^2 + (ay - by)^2

import math as mt

print("Calculando distancia entre 2 puntos:")
print("="*80)

# SOLICITAR LOS DATOS AL USUARIO

ax = float(input("Ingresa la coordenada x del punto A: "))
ay = float(input("Ingresa la coordenada y del punto A: "))

bx = float(input("Ingresa la coordenada x del punto B: "))
by = float(input("Ingresa la coordenada y del punto B: "))

# CALCULAR LA DISTANCIA USANDO LA FORMULA
d = mt.sqrt((ax - bx)**2+(ay - by)**2)

# IMPRIMIR SALIDA
print("-"*80)
print(f"La distancia entre el punto A({ax}, {ay}) y el punto B({bx}, {by}) es: {d:.2f}")
print("="*80)