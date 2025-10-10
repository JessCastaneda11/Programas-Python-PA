# p080-combina-colores

# Genera las combinaciones posibles entre colores

# colores = ['rojo', 'verde', 'azul']

print('\033[2J\033[H')
print("Combinaciones posible de varios colores")
colores = input("Colores separados por coma: ").strip().split(",")

for i in colores:
    for j in colores:

        if i != j:
            print(f"{i} - {j}")