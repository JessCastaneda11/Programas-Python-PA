# p111-lote-autos

# Crear una lista de diccionarios

autos = [
    { 'marca':'Ford', 'modelo':'Mustang', 'año': 1964 },
    { 'marca':'VW', 'modelo':'Jetta', 'año': 2015 }
]

print('\033[2J\033[H')
print("Listado de autos\n")

print(f"\nAutos: {autos} - {len(autos)}")

autos.append({'marca':'Honda', 'modelo':'CVR', 'año':2024})

print(f"\nAutos: {autos} - {len(autos)}")

print("\nCada auto dentro de los autos: ")

for auto in autos:
    print(auto)

print(f"\n\nDatos de los autos en forma de tabla")
print("-"*50)

for k in autos[0].keys():
    print(f'{k}\t\t', end='')

print()
print("-"*50)

for auto in autos:
    for v in auto.values():
        print(f'{v}\t\t', end='')
    print()
print("-"*50)

print("\n\nDatos en forma de registro")
print("-"*50)
suma = 0
for auto in autos:
    suma = suma + auto['año']
    for k,v in auto.items():
        print(f"{k:<12} : {v:>12}")
    print()
print("-"*50)

print(f"\nSuma de los años: ", suma)