# p059-pares-descendente

# Imprimir los números pares y su suma total en un rango descendente desde 100 hasta un número n que elija el usuario.

while True:
    print('\033[H\033[J')
    print("Imprimir números pares en orden descendente\n")
    print("-"*60)

    limite = int(input("Introduce un número límite (Que sea menor a 100): ")) # Hasta donde se hara la cuenta
    
    numero = 100     # Que inicie en 100
    suma = 0

    print("\nNúmeros pares:", end=" ")

    while numero >= limite:
        if numero % 2 == 0:  # Verificar si es número par
            print(numero, end=" ")

            suma += numero
        numero -= 1   # Decrementar para cuenta descendente
    
    print(f"\nLa suma de los pares es: {suma}")

    if input("\n¿Desea continuar (S/N)? ").upper() == "N": break

print("\nProceso Terminado")