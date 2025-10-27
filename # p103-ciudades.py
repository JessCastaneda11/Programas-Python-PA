# p103-ciudades

# Leer nombres de ciudades en una lista, continuando hasta que el usuario introduzca el carácter $. Imprimir:
# • Cuántos elementos tiene la lista.
# • La lista completa.
# • La lista ordenada en orden descendente.
# • Cuántas ciudades inician con una letra consonante y sus nombres.

print('\033[2J\033[H')
print("Lista de Ciudades\n")

ciudades = []
ciudad = ""

while True:
    ciudad = input("Introduzca nombre de ciudad ($ para detener): ")
    if ciudad == "$": break
    ciudades.append(ciudad)

print("\n--- Resultados ---")
print(f"Total de ciudades introducidas: {len(ciudades)}")
print(f"Lista original: {ciudades}")

lista_desc = sorted(ciudades, reverse=True)
print(f"\nLista ordenada descendente: {lista_desc}")

consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
ciudades_consonante = []
i = 0

while i < len(ciudades):
    if ciudades[i][0] in consonantes:
        ciudades_consonante.append(ciudades[i])
    i += 1

print(f"\nCiudades que inician con consonante: {len(ciudades_consonante)}")
print(f"Lista de ciudades con consonante inicial: {ciudades_consonante}")

print("\nProceso Terminado.")