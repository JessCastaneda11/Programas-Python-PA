# p068-conteo-ascendente-for-v2

# Imprime los números de 1 a n, en incrementos de m usando un ciclo for

print('\033[2J\033[H')
print("Iniciando secuencia ascendente")

n = int(input("¿Hasta dónde? "))
m = int(input("¿De cuanto en cuanto? "))

for f in range(1, n+1, m):
    print(f, end=" ")