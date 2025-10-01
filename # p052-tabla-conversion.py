# p052-tabla-conversion

# Mostrar una tabla de conversión de peso a dólares

tc = 20.71

while True:
    print('\033[2J\033[H')
    print("Tabla de conversión de peso a dólar")
    print(f"Tipo de cambio: {tc} pesos x dólar")
    print("-" * 15)

    while True: #Valida los valores inicial y final
        pi = float(input("Valor inicial: "))
        pf = float(input("Valor final: "))

        if (pi > 0 and pf > 0) and (pi < pf): break
        print("Error en los valores de entrada, intenta de nuevo")

    c = pi
    print("\nPesos\t\tDolar")
    print("-"*25)
    while c <= pf:
        print(f"{c:.2f}\t\t{c/tc:.2f}")
        c += 1
        print("-"*25)

    if input("¿Deseas continuar? (S/N)").upper() == 'N': break

print("\nProceso Terminado...")