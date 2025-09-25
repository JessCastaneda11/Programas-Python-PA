# p039-numeros-romanos

# Escribe un programa que pida al usuario un número entero entre 1 y 10 y muestre su equivalente en números romanos. Si el número está fuera de este rango, debe mostrar un mensaje de error.

print('\033[2J\033[H')
print('--- NUMEROS ROMANOS ---')

numero = int(input("Dame un numero del 1 al 10: "))

if numero == 1:
    print("\nI")

elif numero == 2:
    print("\nII")

elif numero == 3:
    print("\nIII")

elif numero == 4:
    print("\nIV")

elif numero == 5:
    print("\nV")

elif numero == 6:
    print("\nVI")

elif numero == 7:
    print("\nVII")

elif numero == 8:
    print("\nVIII")

elif numero == 9:
    print("\nIX")

elif numero == 10:
    print("\nX")

else:
    print("\nError: Número Inválido.")

print("\nProceso Terminado...")