# p031-2da-ley-de-newton

# Calcular la segunda ley de Newton.
# Fuerza = Masa * Aceleración
# Masa = Fuerza / Aceleración
# Aceleración = Fuerza / Masa

print('\033[2J\033[H')
print('--- Calcular los valores de la segunda ley de Newton ---')
print("[F]uerza      = Masa * Aceleración")
print("[M]asa        = Fuerza / Aceleración")
print("[A]celeración = Fuerza / Masa")

opcion = input("\nElige una opción: ").upper()

if opcion == "F":
    print("\nCalculando la Fuerza")
    masa = float(input("Masa: "))
    aceleracion = float(input("Aceleración: "))
    fuerza = masa * aceleracion
    print(f"\nLa fuerza es: {fuerza} ")

elif opcion == "M":
    print("\nCalculando la Masa")
    fuerza = float(input("Fuerza: "))
    aceleracion = float(input("Aceleración: "))
    masa = fuerza / aceleracion
    print(f"\nLa masa es: {masa} ")

elif opcion == "A":
    print("\nCalculando la Aceleración")
    fuerza = float(input("Fuerza: "))
    masa = float(input("Masa: "))
    aceleracion = fuerza / masa
    print(f"\nLa aceleración es: {aceleracion} ")

else:
    print("\nOpción Invalida, elige F, M o A")

print("\nProceso Terminado...")