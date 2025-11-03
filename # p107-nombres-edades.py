# p107-nombres-edades

# Gestión de nombres y edades simulando un censo, con diccionarios

print('\033[2J\033[H')
print("Gestión de nombres y edades simulando un censo, con diccionarios")

datos = {}

print("Introduce nombres y edades (nombre vacío para terminar)")

while True:
    nombre = input("Dame el nombre: ")

    if nombre == '': break

    datos[nombre] = int(input("Edad: "))

print(f"\nCenso de nombres y edades: {datos} - {len(datos)}")

s = 0

for n, e in datos.items():
    print(f"{n:<20} - {e:>2}")
    s = s + e

print(f"\nLa suma es: {s}")
print(f"\nEl promedio es: {s/len(datos):.2f}")