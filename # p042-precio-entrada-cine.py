# p042-precio-entrada-cine

# Crea un programa para la taquilla de un cine que determine el precio de una entrada según la edad del cliente. El programa debe solicitar la edad y mostrar el precio correspondiente, siguiendo estas reglas:
# Menores de 5 años: Entran gratis.
# Niños (5 a 12 años): Pagan $5.
# Adultos (13 a 64 años): Pagan $10.
# Tercera edad (65 años o más): Pagan $7.

print('\033[2J\033[H')
print('--- ENTRADA AL CINE  ---')

edad = int(input("\nIngresa tu edad para saber el costo de tu entrada: "))

if edad < 5:
    print("\nTu entrada es gratis.")

elif edad <= 12:
    print("\nEl precio de tu entrada es de $5.")

elif edad <= 64:
    print("\nEl precio de tu entrada es de $10.")

else:
    print("\nEl precio de tu entrada es de $7.")

print("\nProceso Terminado...")