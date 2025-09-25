# p045-conteo-ascendente-v2

#Imprime los números del 1 a n usando un ciclo while

print('\033[2J\033[H')
print("Iniciando secuencia ascendente...")

n = int(input("Hasta donde? "))
m = int(input("De cuanto en cuanto? "))
c = 1

while c <= n :
    print(f' {c}',end='')
    c += m

print("\n Secuencia Completada")