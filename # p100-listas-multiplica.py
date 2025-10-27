# p100-listas-multiplica

# Leer dos listas, cada una con 5 elementos numéricos. Crear una tercera lista multiplicando los elementos de las dos listas correspondientes. Imprimir las tres listas.

print('\033[2J\033[H')
print("Procesar Listas\n")

entrada_a = input("Introduzca 5 números para la Lista A: ")
entrada_b = input("Introduzca 5 números para la Lista B: ")

lista_a = entrada_a.split()
lista_b = entrada_b.split()

i = 0
lista_c = []
while i < 5:
    a = int(lista_a[i])
    b = int(lista_b[i])
    lista_c.append(a * b)
    i += 1

print("\n--- Resultados ---")
print(f"Lista A: {[int(x) for x in lista_a]}")
print(f"Lista B: {[int(x) for x in lista_b]}")
print(f"Lista C (A * B): {lista_c}")
