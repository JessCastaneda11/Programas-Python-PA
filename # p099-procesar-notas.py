# p099-procesar-notas

# Leer un número indeterminado de notas (calificaciones) entre 0 y 100, deteniéndose cuando el usuario introduzca un 0. Validar que todas las notas introducidas estén dentro del rango [0,100].

# Calcular e imprimir:
# • Cuántas notas se introdujeron.
# • La lista de notas completa.
# • La suma y el promedio de las notas.
# • La nota máxima y la nota mínima.
# • Cuántas notas y cuáles son las notas menores al promedio.


while True:
    print('\033[2J\033[H')
    print("Procesar Notas de Estudiantes\n")

    notas = [] 

    while True:
        nota = float(input("Introduce nota (0 para detener): "))

        if nota == 0: break

        elif nota < 0 or nota > 100:
            print("← Entrada inválida, debe ser entre 0 y 100")
        else:
            notas.append(nota)

    print("\n--- Resultados ---")

    if len(notas) == 0:
        print("No se introdujeron notas.")
    else:
        total = len(notas)
        suma = sum(notas)
        promedio = suma / total
        maxima = max(notas)
        minima = min(notas)

        menores = [n for n in notas if n < promedio]

        print(f"Total de notas introducidas: {total}")
        print(f"Lista de notas: {notas}")
        print(f"Suma de notas: {suma:.0f}")
        print(f"Promedio de notas: {promedio:.1f}")
        print(f"Nota máxima: {maxima}")
        print(f"Nota mínima: {minima}")
        print(f"Notas menores al promedio ({promedio:.1f}): {len(menores)}")
        print(f"Lista de notas menores al promedio: {menores}")

    continuar = input("\n¿Deseas procesar otro grupo de notas? (S/N): ").upper()
    if continuar == "N": break

print("\nProceso Terminado.")