""""
Objetivo: Programa para calcular y registrar las ventas de una papalería
Autor: Jessica Castañeda
Fecha: 2 de Octubre 2025
"""
print("\033[H\033[J")
ventas = cantidad = subtotal = 0
cantidad_c = cantidad_o = cantidad_d = cantidad_p = 0
total_c = total_o = total_d = total_p = 0

while True:
    ventas += 1
    print(f"\nVentas {ventas}")

    tipo = input("Tipo de copia: (C)arta $3.00, (O)ficio $4.00, (D)oble Of $6.00, (P)lano $12.00 ").upper()

    if tipo not in 'CODP':
        err = input(">>>> Error!! Tipo de copia no válido, intente de nuevo, <Enter>")
        ventas -= 1
        continue

    cantidad = int(input("Cantidad: "))
    descuento = 1
    if cantidad > 50:
        descuento = 0.90
        print("** Descuento del 10% aplicado por volumen de venta **")

    if tipo == 'C':
        cantidad_c += cantidad
        subtotal = (cantidad * 3) * descuento
        total_c += subtotal
    
    elif tipo == 'O':
        cantidad_o += cantidad
        subtotal = (cantidad * 4) * descuento
        total_o += subtotal
    
    elif tipo == 'D':
        cantidad_d += cantidad
        subtotal = (cantidad * 6) * descuento
        total_d += subtotal

    elif tipo == 'P':
        cantidad_p += cantidad
        subtotal = (cantidad * 12) * descuento
        total_p += subtotal



    if input("¿Otra venta? (S/N)").upper() != 'S': break

total_copias = cantidad_c + cantidad_o + cantidad_d + cantidad_p
total_ventas = total_c + total_o + total_d + total_p

print("\n-"*60)
print("Resumen diaria de ventas")
print("-"*60)
print(f"Ventas realizadas: {ventas}")
print("-"*60)
print(f"Carta\t\t        :  {cantidad_c:2d}  -  $ {total_c:8.2f}")
print(f"Oficio\t\t        :  {cantidad_o:2d}  -  $ {total_o:8.2f}")
print(f"Doble Oficio\t\t:  {cantidad_d:2d}  -  $ {total_d:8.2f}")
print(f"Plano\t\t        :  {cantidad_p:2d}  -  $ {total_p:8.2f}")
print("-"*60)
print(f"Total ventas \t: {total_copias:2d} - $ {total_ventas:8.2f}")

mensaje_venta = ""

if total_ventas > 150:
    mensaje_venta ="Venta Superada"

elif total_ventas >= 50:
    mensaje_venta = "Venta Frecuente"

else:
    mensaje_venta = "Venta Moderada"

print(f"Esta venta es una: {mensaje_venta}")


print("\nFin de las ventas por este día")