# p073-suma-promedio-numeros

# Suma y promedia n números introducidos por el usuario

while True:
    print('\033[2J\033[H')
    print("Sumando y promediando números")

    n = int(input("\n¿Cuántas calificaciones? "))
    suma = 0
    numeros = ""

    for i in range(1, n+1):
        cal = int(input(f"Calificación {i}: "))
        suma += cal
        #numeros = numeros + str(cal) + " "
        numeros += str(cal) + " "
    
    print(f"\nLas calificaciones fueron: {numeros}")
    print(f"La suma es: {suma}")
    print(f"El promedio es: {suma/n}")

    if input("\n¿Deseas continuar? (S/N) ").upper() == "N": break

print("\nProceso Terminado... ")
