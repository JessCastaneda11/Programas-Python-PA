# p077-triangulo-caracter

# Imprime un triángulo rectángulo de n renglones del caracter deseado

print('\033[2J\033[H')
print("Imprimiendo triángulos con caracteres")

n = int(input("¿Cuántos renglones? "))
c = input("¿De qué caracter? ")

# El bucle exterior se ejecuta N veces
for i in range(1, n + 1):
    # Por cada iteración del bucle exterior, el bucle interior se ejecuta M veces.
    for j in range(1, i):
        # Aquí se ejecutan las acciones anidadas
        print(f"{c}", end="")
    print()