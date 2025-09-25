# p037-numero-mayor

# Escribe un programa que reciba tres números enteros e identifique y muestre cuál de ellos es el mayor.

print('\033[2J\033[H')
print("--- COMPARANDO NUMEROS ---")

print("\nDigita 3 números: ")
numero_1 = int(input("\nNúmero 1: "))
numero_2 = int(input("Número 2: "))
numero_3 = int(input("Número 3: "))

if numero_1 == numero_2 == numero_3:
    print(f"\nLos numeros {numero_1}, {numero_2} y {numero_3} son iguales")

elif numero_1 > numero_2 and numero_1 > numero_3 :
    print(f"\nEl numero mayor es: {numero_1}")

elif numero_2 > numero_1 and numero_2 > numero_3 :
    print(f"\nEl numero mayor es: {numero_2}")

else:
    print(f"\nEl numero mayor es: {numero_3}")

print("\nProceso Terminado...")