# p058-impares-ascendente

# Imprimir los números impares y su suma total en un rango ascendente desde 1 hasta un número n que elija el usuario.

while True:
    print('\033[H\033[J')
    print("Imprimir números impares en orden ascendente\n")
    print("-"*60)

    limite = int(input("Introduce un número límite: ")) # Hasta donde se hara la cuenta
    
    numero = 1      # Que inicie en 1
    suma = 0

    print("\nNúmeros impares:", end=" ")

    while numero <= limite:
        if numero % 2 != 0: # Al dividir entre 2 podemos asumir si el número es par o impar (Si hay residuo es impar)
            print(numero, end=" ")

            suma += numero
        numero += 1

    print(f"\nLa suma de los impares es: {suma}")

    if input("\nDeseas continuar? (S/N)").upper() == 'N': break

print("\nProceso Terminado")