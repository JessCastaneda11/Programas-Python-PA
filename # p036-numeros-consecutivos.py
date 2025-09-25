# p036-numeros-consecutivos

# Escribe un programa que reciba tres números enteros y determine si son consecutivos. Si lo son, muestra un mensaje de confirmación; de lo contrario, informa que no lo son.

print('\033[2J\033[H')
print("--- NÚMEROS CONSECUTIVOS ---")

print("\nDigita 3 números: ")
numero_1 = int(input("\nNúmero 1: "))
numero_2 = int(input("Número 2: "))
numero_3 = int(input("Número 3: "))

if (numero_2 - numero_1) == 1 and (numero_3 - numero_2) == 1:
    print(f"\nLos números {numero_1}, {numero_2} y {numero_3} son consecutivos")

else:
    print(f"\nLos números {numero_1}, {numero_2} y {numero_3} no son consecutivos")
    
print("\nProceso Terminado...")