# p079-factorial-numeros

# Calcula el factorial de n números

print('\033[2J\033[H')
print("Calcular el factorial de 1 a n")

try:
    n = int(input("¿Cuántos factoriales? "))

    for i in range(1, n+1):
        factorial = 1
        for j in range(1, i+1):
            factorial *= j

        print(f"\nFactorial de {i} es = {factorial}")

except ValueError:
    print("\nERROR: Se esperaba un número entero")