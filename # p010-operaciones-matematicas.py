# p010-operaciones-matematicas
# Demostrar el uso de los diferentes operadores aritméticos con números

print("="*90)
print("Calculadora de Operaciones Matemáticas")
print("="*90)

# ENTRADA
X = float(input("Valor de X:"))
Y = float(input("Valor de Y:"))

# SALIDA
print(f"Suma          : {X:>15.2f}  + {Y:<15.2f} = {X + Y:>15.2f}")
print(f"Resta         : {X:>15.2f}  - {Y:<15.2f} = {X - Y:>15.2f}")
print(f"Multiplicación: {X:>15.2f}  * {Y:<15.2f} = {X * Y:>15.2f}")
print(f"División      : {X:>15.2f}  / {Y:<15.2f} = {X / Y:>15.2f}")
print(f"Módulo        : {X:>15.2f}  % {Y:<15.2f} = {X % Y:>15.2f}")
print(f"Div. Entera   : {X:>15.2f} // {Y:<15.2f} = {X // Y:>15.2f}")

print("="*90)