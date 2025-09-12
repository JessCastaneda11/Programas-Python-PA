# p022-resistencia-equivalente-paralelo

# Crea un programa que calcule la resistencia total o equivalente de un circuito
# con cuatro resistencias en paralelo.
# El programa debe solicitar al usuario que ingrese el valor de cada una de las cuatro resistencias 
# (R1, R2, R3 y R4).
# Luego, debe calcular la resistencia total usando la siguiente fórmula:
# RT = 1 / ((1/R1) + (1/R2) + (1/R3) + (1/R4))

print("Calculando resistencia total (RT):")
print("="*80)

# SOLICITAR LOS DATOS AL USUARIO
R1 = float(input("Ingresa el valor de la Resistencia 1: "))
R2 = float(input("Ingresa el valor de la Resistencia 2: "))
R3 = float(input("Ingresa el valor de la Resistencia 3: "))
R4 = float(input("Ingresa el valor de la Resistencia 4: "))

# CALCULANDO LA RESISTENCIA TOTAL
RT = 1 / ((1/R1) + (1/R2) + (1/R3) + (1/R4))

# IMPRIMIR SALIDA
print("-"*60)
print(f"La resistencia total es de: {RT:.2f} ohms")
print("="*60)