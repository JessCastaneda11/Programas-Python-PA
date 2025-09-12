# p016-tercer-angulo

# Escribir un programa que determine el tercer ángulo de un triángulo.
# El programa debe pedir al usuario que ingrese las medidas de dos ángulos del triángulo. 
# Utiliza la siguiente fórmula para encontrar el ángulo faltante:
# Angulo3 = 180 – (Angulo1 + Angulo2)

print("="*80)
print("Determinando el tercer ángulo de un triángulo:")
print("-"*80)

# SOLICITAR LOS DATOS AL USUARIO
Angulo1 = float(input("Ingresa el valor del Ángulo 1:"))
Angulo2 = float(input("Ingresa el valor del Ángulo 2:"))
print("-"*80)

# CALCULO DEL 3ER ÁNGULO
Angulo3 = 180 - (Angulo1 + Angulo2)

# IMPRIMIR SALIDA
print(f"El valor del 3er ángulo es: {Angulo3:.2f}")
print("="*80)