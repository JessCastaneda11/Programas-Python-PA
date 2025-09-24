# p035-tipo-triangulo

# Objetivo: Clasificar un triángulo según la longitud de sus lados.
# Lados iguales = Equilatero, 2 Lados iguales = Isoceles, Lados diferentes = Escaleno

print('\033[2J\033[H')
print("--- CLASIFICADOR DE TRIÁNGULOS ---")

lado_a = float(input("Lado A: "))
lado_b = float(input("Lado B: "))
lado_c = float(input("Lado C: "))

if lado_a == lado_b == lado_c:
    print("Es un triángulo EQUILATERO, dado que todos sus lados son iguales")

elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("Es un triángulo ISOCELES, dado que solo 2 de sus lados son iguales")

else:
    print("Es un triángulo ESCALENO, dado que los 3 lados son diferentes")

print("\nProceso Terminado...")