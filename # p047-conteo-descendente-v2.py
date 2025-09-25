# p047-conteo-descendente-v2

# Imprime los números de n a 1 usando un ciclo while

print('\033[2J\033[H')
print("Iniciando cuenta regresiva ...")

n = int(input("Desde dónde? "))
m = int(input("De cuanto en cuanto? "))
c = n

while c >= 1:
    print(f' {c}', end='')
    c -= m

print("\n Terminado...")