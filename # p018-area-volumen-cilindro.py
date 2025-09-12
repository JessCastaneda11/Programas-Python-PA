# p018-area-volumen-cilindro

# Crea un programa que calcule el área y volumen de un cilindro.
# Pide al usuario que ingrese el radio y la altura del cilindro.
# Las fórmulas para el cálculo de área y de volumen son:
# Area = 2PI * radio * (radio + alto)
# Volumen = PI * (Radio * Radio) * Altura

import math as mt

print("Calculando el área y el volumen de un cilindro:")
print("="*80)

# SOLICITAR LOS DATOS AL USUARIO
r = float(input("Ingresa el valor del radio:"))
h = float(input("Ingresa el valor de la altura:"))
print("-"*80)

# CALCULOS
A = 2 * mt.pi * r * (r + h)
V = mt.pi * (r**2) * h

#IMPRIMIR SALIDAS
print(f"El área del cilindro de radio {r:.2f} y altura {h:.2f} es: {A:.2f}")
print(f"El volumen del cilindro de radio {r:.2f} y altura {h:.2f} es: {V:.2f}")
print("="*80)