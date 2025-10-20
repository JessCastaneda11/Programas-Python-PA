# p087-acceder-lista

# Acceder a los elementos de una lista por su índice

nums = [10,20,30,40,60,70,10,20,99]

print('\033[2J\033[H')
print("Acceder a los elementos de una lista")
print("Longitud y contenido")
print(f"¿Cuántas mediciones son? {len(nums)}")
print(f"Todas las mediciones: {nums}")

print("\nPrimera y última medición por índice positivo")
print(f"La primera: {nums[0]}")
print(f"La última : {nums[8]}")

print("\nPrimera y última medición por índice negativo")
print(f"La primera: {nums[-9]}")
print(f"La última : {nums[-1]}")

print("\nPor Rango: ")
print(f"Las mediciones de la 2 a la 6 (sin incluir la 6): {nums[2:6]}")

print("\nPor saltos consecutivos: ")
print(f"Las primeras 3 mediciones, iniciando de la izquierda: {nums[:3]} ")
print(f"Las últimas 3 mediciones, desde la 6 hasta el final : {nums[6:]} ")