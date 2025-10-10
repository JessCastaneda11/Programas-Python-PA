#p078-piramide-caracter

# Imprime una piramide de caracteres

print('\033[2J\033[H')
print("Imprimiendo piramides de caracteres")

n = int(input("¿Cuántos renglones? "))
c = input("¿De qué caracter? ")

# El bucle exterior se ejecuta N veces
for i in range(1, n + 1):
    espacios = n - i
    for k in range(espacios):
        print(" ", end="")

    caracteres = 2 * i - 1
    # Por cada iteración del bucle exterior, el bucle interior se ejecuta M veces.
    for j in range(caracteres):
        # Aquí se ejecutan las acciones anidadas
        print(f"{c}", end="")
    print()