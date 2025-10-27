# p101-mes-día-nombre

# Leer un número de mes (ej. 4). Guardar los días de cada mes en una lista y los nombres de los meses en otra lista. Asumir 28 días para febrero. Imprimir el nombre del mes y la cantidad de días del mes correspondiente (ej. marzo, 30).

print('\033[2J\033[H')
print("Mes y Días Correspondientes\n")

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

numero_mes = int(input("Introduzca un número de mes (1-12): "))


if numero_mes >= 1 and numero_mes <= 12:
    indice = numero_mes - 1
    print("\n--- Resultados ---")
    print(f"Mes: {meses[indice]}")
    print(f"Días: {dias[indice]}")
    
else:
    print("\nNúmero inválido. Debe estar entre 1 y 12.")

print("\nProceso Terminado.")