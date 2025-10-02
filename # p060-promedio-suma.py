# p060-promedio-suma

# Leer números introducidos por el usuario hasta que ingrese un 0. Al finalizar, mostrar el conteo total de números, la suma y el promedio de la serie.


while True:
    print("\033[H\033[J")
    print("Conteo de números (0 para terminar)")
    print("-"*60)

    suma = 0
    conteo = 0

    while True:
        numero = int(input("Ingresa un número: "))
        if numero == 0: break

        suma += numero
        conteo += 1

    print("-"*60)
    print(f"\nLa cantidad de números es {conteo}")
    print(f"\nLa suma es: {suma}")

    if conteo > 0:
        promedio = suma / conteo
        print(f"El promedio es: {promedio:.2f}")

    else:
        print("Por favor introduce números válidos.")


    if input("\n¿Desea continuar (S/N)? ").upper() == "N": break

print("\nProceso Terminado")
