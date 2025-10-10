# p076-tablas-todas

# Imprime todas las tablas de 1 a n, hasta m

print('\033[2J\033[H')
print("Imprimiendo las tablas de multiplicar de 1 a n, hasta m")

n = int(input("¿Hasta qué tabla? "))
m = int(input("¿Hasta qué multiplicador? "))

# El bucle exterior se ejecuta N veces
for i in range(1, n + 1):
    print(f"---- Tabla del {i} ---- ")
    # Por cada iteración del bucle exterior, el bucle interior se ejecuta M veces.
    for j in range(1, m + 1):
        # Aquí se ejecutan las acciones anidadas
        print(f"{i} x {j} = {i * j}")
    print("\n")