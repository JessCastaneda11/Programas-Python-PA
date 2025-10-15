# p084-cuadro-hueco-caracter

# El programa debe solicitar al usuario que ingrese el tamaño del lado de un cuadrado y el carácter con el que se dibujará. Luego, deberá imprimir en la consola un "cuadrado hueco", donde el carácter solo se utilice para dibujar el contorno del mismo.

while True:
    print('\033[2J\033[H')  # Limpia la pantalla
    print("Dibujo de un Cuadro Hueco con Caracteres\n")

    lado = int(input("¿De qué tamaño será el lado del cuadrado? "))
    caracter = input("¿Qué carácter quieres usar? ")
    print()

    for fila in range(lado):
        for columna in range(lado):
            if fila == 0 or fila == lado - 1 or columna == 0 or columna == lado - 1:
                print(caracter, end=" ")
            else:
                print(" ", end=" ")
        print()

    continuar = input("\n¿Deseas dibujar otro cuadrado? (S/N): ").upper()
    if continuar == "N": break

print("\nProceso Terminado...")