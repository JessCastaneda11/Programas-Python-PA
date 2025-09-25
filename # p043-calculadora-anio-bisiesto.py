# p043-calculadora-año-bisiesto

# Problema: Escribe un programa que determine si un año, ingresado por el usuario, es bisiesto. Un año es bisiesto si cumple una de las siguientes condiciones:
# 1. Es divisible por 4, pero no es divisible por 100.
# 2. Es divisible por 400.
# El programa debe indicar claramente si el año es bisiesto o no.

print('\033[2J\033[H')
print('--- CALCULADORA DE AÑO BISIESTO  ---')

año = int(input("\nIngresa un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"\nEl año {año} es bisiesto.")

    if año % 400 == 0:
        print("\nPorque es divisible por 400.")

    else:
        print("\nPorque es divisible por 4 pero no por 100.")

else:
    print(f"\nEl año {año} no es bisiesto.")

    if año % 100 == 0:
        print("\nPorque es divisible por 100 pero no por 400.")

    else:
        print("\nPorque no es divisible por 4.")

print("\nProceso Terminado...")