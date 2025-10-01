# p055-tabla-multiplicar-while-v2

# Imprime las tablas de 1 a n, desde 1 hasta m

while True:
    print('\033[2J\033[H')
    print("\nTablas de Multiplicar")

    while True:
        n = int(input("¿Hasta qué tabla quieres? "))
        m = int(input("¿Hasta dónde la quieres? "))

        if n > 0 and m > 0: break
        print("Valores incorrectos")
    
    t = 1

    while t <= n:
        print(f"\nTabla {t}")

        c = 1

        while c <= m:
            print(f"{t} x {c} = {t * c}")
            c += 1

        t += 1


    if input("\n¿Deseas continuar? (S/N)").upper() == 'N': break
    
print("\nProceso Terminado...")