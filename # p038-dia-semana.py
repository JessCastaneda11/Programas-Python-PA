# p038-dia-semana

# Escribe un programa que solicite un número entero del 1 al 7 y muestre el día de la semana correspondiente, considerando que 1 es domingo y 7 es sábado. Si el número ingresado está fuera de ese rango, debe mostrar un mensaje de error.

print('\033[2J\033[H')
print('--- Dias de la Semana ---')

dia = int(input("Dame un numero del 1 al 7: "))

if dia < 1 or dia > 7:
    print("\nError: DIA INVALIDO")

elif dia == 1:
    print("\nDomingo")

elif dia == 2:
    print("\nLunes")

elif dia == 3:
    print("\nMartes")

elif dia == 4:
    print("\nMiércoles")

elif dia == 5:
    print("\nJueves")

elif dia == 6:
    print("\nViernes")

else:
    print("\nSábado")

print("\nProceso Terminado...")