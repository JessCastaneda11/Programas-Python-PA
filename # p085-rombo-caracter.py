# p085-rombo-caracter

# Solicitar al usuario un número entero impar n que representará la altura y el ancho máximo de un rombo. El programa deberá dibujar el rombo utilizando el carácter que el usuario elija.

while True:
    print('\033[2J\033[H')
    print("Dibujo de un Rombo con Caracteres\n")

    n = int(input("Dame un número impar para la altura: "))
    caracter = input("¿Qué carácter quieres usar? ")

   
    if n % 2 == 0:  # Validar que el número sea impar
        print("\nEl número debe ser impar. Intenta nuevamente.")

    else:
        print()
        mitad = n // 2

        # Parte superior del rombo
        for i in range(mitad + 1):
            print(" " * (mitad - i) + caracter * (2 * i + 1))

        # Parte inferior del rombo
        for i in range(mitad - 1, -1, -1):
            print(" " * (mitad - i) + caracter * (2 * i + 1))

    continuar = input("\n¿Deseas dibujar otro rombo? (S/N): ").upper()
    if continuar == "N": break

print("\nProceso Terminado...")