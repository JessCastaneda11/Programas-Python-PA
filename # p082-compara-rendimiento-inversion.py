# p082-compara-rendimiento-inversion

# Desarrolla un programa que compare el crecimiento de dos fondos de inversión a lo largo de varios años. El usuario debe ingresar el monto inicial y la tasa de interés anual (porcentaje) para cada uno de los dos fondos, así como el número de años a proyectar. El programa deberá mostrar una tabla comparativa anual y al final indicar qué fondo generó un mayor rendimiento.

print('\033[2J\033[H')  # Limpia pantalla
print("Comparación de Rendimiento de Fondos de Inversión\n")


print("--- Fondo de Inversión A ---") # Pedir datos para el primer fondo "A"
monto_a = float(input("Monto inicial: "))
tasa_a = float(input("Tasa de interés anual (%): "))

print("\n--- Fondo de Inversión B ---") # Pedir datos para el segundo fondo "B"
monto_b = float(input("Monto inicial: "))
tasa_b = float(input("Tasa de interés anual (%): "))

print()
años = int(input("Años a proyectar: "))

print("\n--- Comparación de Rendimientos Anuales ---") # Encabezado de tabla
print("Año |   Fondo A   |   Fondo B")
print("-------------------------------")

for año in range(1, años + 1):
    monto_a += monto_a * tasa_a / 100
    monto_b += monto_b * tasa_b / 100
    print(f"{año:2}  |  ${monto_a:8.2f}  |  ${monto_b:8.2f}")

print("\n--------------------------------------------")

if monto_a > monto_b:
    print(f"Resultado final: El Fondo A (${monto_a:.2f}) superó al Fondo B (${monto_b:.2f}).")

elif monto_b > monto_a:
    print(f"Resultado final: El Fondo B (${monto_b:.2f}) superó al Fondo A (${monto_a:.2f}).")
    
else:
    print(f"Resultado final: Ambos fondos alcanzaron el mismo valor (${monto_a:.2f}).")

print("\nProceso Terminado...")