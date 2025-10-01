# p054-tabla-multiplicar-while-v1

# Imprime la tabla de multiplicar t hasta n

while True:
    print('\033[2J\033[H')
    print("Imprime la tabla de multiplicar t hasta n")

    while True:
        t = int(input("Tabla: "))
        n = int(input("Hasta dónde? "))

        if t > 0 and n > 0: break
        print("Error, los valores son incorrectos")
    
    c = 1

    while c <= n:
        print(f"{t} x {c} = {t * c:5}")
        c += 1


    if input("\n¿Deseas continuar? (S/N)").upper() == 'N': break

print("\nProceso Terminado...")