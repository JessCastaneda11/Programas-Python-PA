# p020-numero-suerte

# Escribe un programa que solicite al usuario su año de nacimiento como un número entero de cuatro dígitos.
# A partir de este dato, el programa debe:
# - Mostrar cada uno de los dígitos individuales del año. 
# Por ejemplo, si el año es 1995, debe mostrar "1", "9","9", "5".
# - Calcular y mostrar la suma de los dígitos individuales del año.
# Siguiendo el ejemplo anterior, la suma sería: 1 + 9 + 9 + 5 = 24.

print("Número de la suerte")
print("="*80)

# SOLICITAR LOS DATOS AL USUARIO
año = int(input("Por favor ingresa tu año de nacimiento: "))
print("-"*80)

# SEPARANDO LOS DIGITOS
digito1 = año // 1000
digito2 = (año % 1000) // 100
digito3 = (año % 100) // 10
digito4 = año % 10

suma = (digito1 + digito2 + digito3 + digito4)

# IMPRIMIR SALIDA
print(f"Tu año de nacimiento es: {año}\n")
print("Los digitos individuales son:")
print(digito1)
print(digito2)
print(digito3)
print(digito4)
print(f"\nY la suma de los 4 digitos individuales es igual a: {suma}")
print("="*80)