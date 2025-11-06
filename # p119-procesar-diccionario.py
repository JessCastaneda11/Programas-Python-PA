# p119-procesar-diccionario

# Define dos listas:
#   - nombres = ['Juan', 'Pedro', 'Manuel', 'Elías', 'María', 'Felipe', 'Julia', 'Roberto']
#   - sueldos = [4550.22, 8456.88, 1235.12, 9980.00, 12345.50, 29456.55, 12234.00, 2000.00]
# Crea un diccionario llamado nomina combinando ambas listas (los nombres como llaves, los sueldos como valores).
# Muestra el diccionario resultante.
# Itera sobre el diccionario y muestra su contenido de cuatro formas:
#   - Mostrando solo las llaves (usando keys()).
#   - Mostrando solo los valores (usando values()).
#   - Mostrando llave y valor accediendo por la llave.
#   - Mostrando llave y valor simultáneamente (usando items()).
# Calcula y muestra:
#   - La suma total de los sueldos.
#   - El promedio de los sueldos.

print('\033[H\033[J')
print("Procesar Diccionario de Nómina\n")

nombres = ['Juan', 'Pedro', 'Manuel', 'Elías', 'María', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9980.00, 12345.50, 29456.55, 12234.00, 2000.00]

nomina = dict(zip(nombres, sueldos))

print("Diccionario de nómina:")
print(nomina)

print("\n--- Iterando Llaves (keys) ---")
for k in nomina.keys():
    print(k)

print("\n--- Iterando Valores (values) ---")
for v in nomina.values():
    print(v)

print("\n--- Iterando Llave y Valor (accediendo por llave) ---")
for k in nomina:
    print(f"{k} -> {nomina[k]}")

print("\n--- Iterando Llave y Valor (items) ---")
for k, v in nomina.items():
    print(f"{k} -> {v}")

suma = sum(nomina.values())
promedio = suma / len(nomina)

print("\n--- Cálculos ---")
print(f"Suma total de sueldos: {suma:.2f}")
print(f"Promedio de sueldos: {promedio:.2f}")