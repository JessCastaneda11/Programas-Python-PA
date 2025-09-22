# p024-verificar-numero-v2

# Verifica si un número es positivo, negativo o cero.

print("Verificando si un número es positivo, negativo o cero")

# ENTRADA
print("Dame un número entero: ")
numero = int(input())

# PROCESO O TOMA DE DECISIÓN
if numero == 0:
    print("El número es 0👌")

else:
    if numero < 0:
        print("El número es negativo👎")
        
    else:
        print("El número es positivo👍")

print("Proceso terminado")