# p113-reporte-ventas

# Crear un diccionario de diccionarios

print('\033[H\033[J')
print('Reporte de Ventas por Clientes\n')

n = int(input("Número de compras a registrar: "))
compras = []

for i in range(n+1):
    print(f"\n----- Compra {i+1} ------")
    compra = {
        'cliente': input("Nombre Cliente: "),
        'producto': input("Producto: "),
        'cantidad': float(input("Cantidad: ")),
        'precio': float(input("Precio: "))
    }
    compras.append(compra)

print("\nLista de compras registradas")
#print(compras)

clientes = {}

for compra in compras:
    cliente = compra['cliente']

    if cliente not in clientes:
        clientes[cliente] = {"cantidad":0, "subtotal":0}

    clientes[cliente]['cantidad'] += compra['cantidad']
    clientes[cliente]['subtotal'] += compra['cantidad'] * compra['precio']

#print(clientes)

for cliente, datos in clientes.items():
    print(f"Cliente  : {cliente}")
    print(f"Cantidad : {datos['cantidad']}")
    print(f"Subtotal : {datos['subtotal']}")