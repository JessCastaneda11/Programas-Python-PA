# p094-consolidar-ventas

# Consolidar la venta de dos sucursales, las ventas las captura el usuario.

print('\033[2J\033[H')
print("Consolidar la venta de dos sucursales.")

ventas = int(input("¿Cuántas ventas por sucursal? "))

ventas1 = []
ventas2 = []
todo = []

print("\nDame las ventas de la primera sucursal: ")
for i in range(ventas):
    venta = int(input(f"Venta del día: {i+1}: "))
    ventas1.append(venta)

print("\nDame las ventas de la segunda sucursal: ")
for i in range(ventas):
    venta = int(input(f"Venta del día: {i+1}: "))
    ventas2.append(venta)

print("\nConsolidando las ventas: ")

for i in range(ventas):
    sumadia = ventas1[i] + ventas2[i]
    todo.append(sumadia)

print("\nReporte de Ventas: ")
print(f"Sucursal 1 : {ventas1}")
print(f"Sucursal 2 : {ventas2}")
print(f"Consolidado : {todo}")