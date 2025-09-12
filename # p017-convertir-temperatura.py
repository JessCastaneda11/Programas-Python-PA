# p017-convertir-temperatura

# Desarrolla un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.
# El programa debe solicitar al usuario una temperatura en Celsius y luego mostrar el resultado en Fahrenheit.
# La fórmula para la conversión es:
# farenheit = (celsius × 9/5) + 32

print("Conversor de temperatura (Celsius - Fahrenheit)")
print("="*80)

# SOLICITAR LOS DATOS AL USUARIO
celsius = float(input("Ingresa la temperatura en Celsius:"))
print("-"*80)

# CALCULO DE CONVERSIÓN
fahrenheit = (celsius * 9 / 5 ) + 32

# IMPRIMIR SALIDA
print(f"{celsius:.2f} grados celsius equivalen a {fahrenheit:.2f} grados fahrenheit")
print("="*80)