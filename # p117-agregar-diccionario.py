# p117-agregar-diccionario

# Crea un diccionario llamado ventas con los siguientes datos: Juan: 1550, Jose: 2600, Maria: 2220.
# Muestra el diccionario inicial.
# Agrega los siguientes vendedores y sus ventas:
#   - Rocio: 2500 (usando []).
#   - Mateo: 1567 (usando []).
#   - Andrea: 9567 (usando update()).
#   - Miguel: 1234 (usando update()).
# Finalmente muestra el diccionario actualizado.

print('\033[H\033[J')
print("Agregar elementos a un diccionario\n")

ventas = {
    "Juan": 1550,
    "Jose": 2600,
    "Maria": 2220
}

print("Ventas iniciales:")
print(ventas)

ventas["Rocio"] = 2500
ventas["Mateo"] = 1567
ventas.update({"Andrea": 9567})
ventas.update({"Miguel": 1234})

print("\nVentas actualizadas:")
print(ventas)