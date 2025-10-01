# p053-conjetura-collatz

# Calcular la conjetura de Collatz

while True:
    print('\033[2J\033[H')
    print("Imprime la conjetura de Collatz")
    pasos = 0

    while True:
        num = int(input("Dame un número entero positivo: "))

        if num > 0: break
        print("Error, el número debe ser positivo")
    
    while True:
        if num == 1: break
        print(num, end=' ')

        if num % 2 == 0:
            num = num // 2
        
        else:
            num = num * 3 + 1
        pasos = pasos + 1

    print(num, end=' ')
    print("\nPasos: " + str(pasos))

    if input("¿Deseas continuar? (S/N)").upper() == 'N': break

print("\nProceso Terminado...")