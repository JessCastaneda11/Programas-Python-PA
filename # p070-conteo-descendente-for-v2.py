# p070-conteo-descendente-for-v2

# Imprime los números de n a 1, en decrementos de m usando un ciclo for

print('\033[2J\033[H')
print("Iniciando secuencia ascendente")

n = int(input("¿Hasta dónde? "))
m = int(input("¿De cuanto en cuanto? "))

for f in range(n, 0, -m):
    print(f, end=" ")