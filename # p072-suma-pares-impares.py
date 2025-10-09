# p072-suma-pares-impares

# Imprimir números pares e impares y su suma, usando un ciclo for

while True:
    print('\033[2J\033[H')

    print("Imprimir números pares o impares y su suma (Ascendente)")
    print("[ 1 ] Pares")
    print("[ 2 ] Impares")
    op = int(input("\nElige una opción: "))

    s = 0

    if op == 1:
        n = int(input("\nLímite: "))
        print(f"\nImprimiendo números pares y su suma")
        for i in range(2, n+1, 2):
            print(i, end=" ")
            s += i
        print("\nSuma de pares: " + str(s))
    
    elif op == 2:
        n = int(input("\nLímite: "))
        print(f"\nImprimendo números impares y su suma")
        for i in range(1, n+1, 2):
            print(i, end=" ")
            s += i
        print("\nSuma de impares: " + str(s))
    
    else:
        print("\n\nOpción Invalida")
        

    if input("\n¿Deseas continuar? (S/N) ").upper() == "N": break

print("\nProceso Terminado... ")