# p064-verificar-palindromo

# Solicitar al usuario que ingrese un número entero y determinar si es un palíndromo. Un número es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda (ej. 121, 3443).


while True:
    print("\033[H\033[J")
    print("Verificando si un número es palíndromo")
    print("-"*60)

    
    numero = input("Introduce un número para verificar si es palíndromo: ")
    posicion = len(numero) - 1
    invertido = ""

    while posicion >= 0:
        invertido = invertido + numero[posicion] 
        posicion -= 1

    if numero == invertido:
        print(f"El número {numero} es un palíndromo.")
    else:
        print(f"El número {numero} no es un palíndromo.")

    if input("\n¿Desea continuar (S/N)? ").upper() == "N": break

print("\nProceso Terminado")