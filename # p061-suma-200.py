#p061-suma-200

# Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200. Al terminar, mostrar cuántos números se introdujeron y la suma final.


while True:
    print("\033[H\033[J")
    print("Sumar los números hasta llegar a 200")
    print("-"*60)

    suma = 0
    conteo = 0

    while suma < 200:
        print(f"Suma actual: {suma}. ", end=" ")
        numero = int(input("Introduce un número: "))
        suma += numero
        conteo += 1

    print("-"*60)
    print("Meta de 200 alcanzada.")
    print(f"Suma total: {suma}")
    print(f"Total de números introducidos: {conteo}")

    if input("\n¿Desea continuar (S/N)? ").upper() == "N": break

print("\nProceso Terminado")