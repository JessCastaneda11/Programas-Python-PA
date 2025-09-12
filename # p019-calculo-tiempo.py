# p019-calculo-tiempo

# Diseña un programa que tome una cantidad de horas como un número entero.
# El programa debe calcular y mostrar el equivalente de ese tiempo en:
# - Días (considerando que 1 día tiene 24 horas)
# - Minutos (considerando que 1 hora tiene 60 minutos)
# - Segundos (considerando que 1 minuto tiene 60 segundos)

print("Calculando días, minutos y segundos...")
print("="*80)

# SOLICITAR LOS DATOS AL USUARIO
h = int(input("Ingrese la cantidad de horas a convertir:"))
print("-"*80)

# CALCULAR LAS CONVERISONES
d = h/24
m = h*60
s = m*60

# IMPRIMIR SALIDAS 
print(f"{h} horas equivalen a {d} días")
print(f"{h} horas equivalen a {m} minutos")
print(f"{h} horas equivalen a {s} segundos")
print("="*80)
