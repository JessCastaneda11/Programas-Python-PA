# p104-lista-impares

# Leer un entero n. Llenar una lista con los primeros n números impares.
# Calcular e imprimir:
# • La suma y el promedio de los números.
# • Los números que son divisibles entre 3 y su suma.
# • Pedir un elemento a buscar en la lista original e indicar si está y en qué posición (índice).


print('\033[2J\033[H')
print("Lista de Números Impares\n")

n = int(input("Introduzca la cantidad de números impares (n): "))

impares = []
i = 1
contador = 0

while contador < n:
    impares.append(i)
    i += 2
    contador += 1

print("\n--- Generación de Lista ---")
print(f"Lista de los primeros {n} números impares: {impares}")

suma_total = 0
i = 0
while i < len(impares):
    suma_total += impares[i]
    i += 1

promedio = suma_total / len(impares)

print("\n--- Cálculos ---")
print(f"Suma de los números: {suma_total}")
print(f"Promedio de los números: {promedio:.1f}")

div3 = []
suma_div3 = 0

i = 0
while i < len(impares):
    if impares[i] % 3 == 0:
        div3.append(impares[i])
        suma_div3 += impares[i]
    i += 1

print("\n--- Divisibles entre 3 ---")
print(f"Números divisibles entre 3: {div3}")
print(f"Suma de los números divisibles entre 3: {suma_div3}")

print("\n--- Búsqueda ---")
buscar = int(input("Introduzca elemento a buscar: "))

if buscar in impares:
    indice = impares.index(buscar)
    print(f"Result: El elemento {buscar} está en la lista en la posición (índice) {indice}.")
else:
    print(f"Result: El elemento {buscar} no está en la lista.")

print("\nProceso Terminado.")