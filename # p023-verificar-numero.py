# p023-verificar-numero

# Verifica si un número es positivo, negativo o cero.

print("Verificando si un número es positivo, negativo o cero")

# ENTRADA
print("Dame un número entero: ")
numero = int(input())

# PROCESO
if numero > 0:
    print("El número es positivo👍")

if numero < 0:
    print("El número es negativo👎")

if numero == 0:
    print("El número es cero👌")

print("Proceso terminado")   