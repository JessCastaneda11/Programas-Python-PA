# p063-numero-mayor

# Leer una serie de números hasta que el usuario ingrese un 0. Al terminar, el programa deberá mostrar cuál fue el número más grande de todos los introducidos.

while True:
    print("\033[H\033[J")
    print("Introduce números (0 para terminar):")
    print("-"*60)

    numero = int(input("> "))  
    mayor = 0

    while numero != 0:
        numero = int(input("> "))
        if numero != 0 and numero > mayor:
            mayor = numero

    print("-"*60)
    print(f"\nEl número mayor fue: {mayor}")

    
    if input("\n¿Desea continuar (S/N)? ").upper() == "N": break

print("\nProceso Terminado")