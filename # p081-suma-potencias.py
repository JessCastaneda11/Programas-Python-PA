# p081-suma-potencias

# Suma de potencias de un número x, desde x^1 hasta x^n

print('\033[2J\033[H')

x = int(input("Valor de x: "))
n = int(input("Valor de n: "))
suma_total = 0

termino_actual = 1
for j in range(n+1):
    suma_total += termino_actual
    print(f"Termino {x}^{j} = {termino_actual}")
    termino_actual *= x

print(f"\nSuma de tota la serie = " , suma_total)