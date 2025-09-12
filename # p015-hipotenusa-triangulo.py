# p015-hipotenusa-triangulo

# Crear un programa que calcule la longitud de la hipotenusa de un triángulo rectángulo. 
# El programa debe solicitar al usuario que ingrese la longitud de los dos lados (catetos) del triángulo.
# Para el cálculo, utiliza la siguiente fórmula:
# Hipotenusa = raizcuadrada( longlado1 * lognlado1 + longlado2 * longlado2 )

import math as mt

print("="*80)
print("Calculando la hipotenusa de un triángulo:")
print("-"*80)

# SOLOCITAR LOS DATOS AL USUARIO
print("Ingresa el valor de los catetos del triángulo separados por un espacio:")

L1, L2 = input().split()
L1, L2 = float(L1), float(L2)
print("-"*80)

# CALCULAR LA HIPOTENUSA
H = mt.sqrt((L1*L1)+(L2*L2))

# IMPRIMIR SALIDA
print(f"El valor de la hipotenusa del triángulo de catetos {L1:.2f} y {L2:.2f} es: {H:.2f} ")
print("="*80)