# p086-triangulo-invertido-numeros

# Solicitar al usuario un número entero n que determinará la altura de un triángulo numérico invertido. El programa debe imprimir n renglones. El primer renglón contendrá los números de 1 a n, el segundo de 1 a n-1, y así sucesivamente hasta que el último renglón contenga solo el número 1.

while True:
    print('\033[2J\033[H')
    print("Triángulo Numérico Invertido\n")

    n = int(input("Dame un número: "))
    print()

    for fila in range(n, 0, -1):     
        for num in range(1, fila + 1):     
            print(num, end=" ")
        print()                            


    continuar = input("\n¿Deseas dibujar otro triángulo? (S/N): ").upper()
    if continuar == "N": break

print("\nProceso Terminado...")