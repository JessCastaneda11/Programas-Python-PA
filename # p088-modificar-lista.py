# p088-modificar-lista

# Muestra como modificar los elementos de una lista

print('\033[2J\033[H')
print("Modificar los elementos de una lista")

califs = [10, 9, 8,5, 6.5, 9.8, 7, 7, 6.2, 9.5]
print(f'\nTodas las calificaciones: {califs} - {len(califs)}')

print("\nModificar la posición [0] y [1] con 7 y 7: ")
califs[0] = 7
califs[1] = 7
print(f"\nResultado: {califs}")

print("\nModificar el rango [2:5] (el 5 no se incluye) con 9, 9, 9: ")
califs[2:5] = [9,9,9]
print(f"\nResultado: {califs}")
