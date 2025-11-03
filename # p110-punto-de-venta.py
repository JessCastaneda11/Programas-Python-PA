# p110-punto-de-venta

# Simular un punto de venta

print('\033[2J\033[H')
print("Simulando un punto de venta...")

menu = {
    'taco': 18.50,
    'burrito': 45.00,
    'quesadilla': 35.00,
    'refresco': 20.00,
    'agua': 15.00
}

print("\n---- Bienvenido al Taco Feroz ----")
print("Este es nuestro menú: ")

for a, p in menu.items():
    print(f"- {a:<12} : ${p:,.2f}")

orden = {}
total_general = 0

while True:
    producto = input("¿Qué deseas? ").lower()

    if producto == 'fin': break

    cantidad = int(input("¿Cantidad? "))
    orden[producto] = orden.get(producto, 0) + cantidad

    print(f"Agregados {cantidad} {producto} a tu orden")

print(f"\nTu orden fue: \n{orden}")

print("\n---- RECIBO ----")

if not orden:
    print("No compraste nada")

else:
    for p, c in orden.items():
        precio_unitario = menu[p]
        subtotal = precio_unitario * c
        print(f"{c} x {p:<12} : ${subtotal:,.2f}")
        total_general += subtotal

print("-"*35)
print(f"TOTAL A PAGAR: ${total_general:,.2f}")
print("GRACIAS POR TU COMPRA!!!")