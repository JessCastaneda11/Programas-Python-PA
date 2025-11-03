# p108-conversor-unidades

# Convertir de diferentes unidades de longitud a metros, usando diccionarios

conv = {
    'km': 1000,
    'm': 1,
    'cm': 0.01,
    'mm': 0.001
}

print('\033[2J\033[H')
print("Convertir de diferentes unidades de longitud a metros, usando diccionarios")


while True:
    try:

        longitud = int(input("Dame la longitud en metros: "))

        break

    except ValueError:
        continue


while True:

    uni = input("A qué unidad deseas convertir (km, m, cm ,mm): ")

    if uni in conv: break

    else: continue

resultado = longitud / conv[uni]

#print(f"{longitud:,.2f} {uni} son {resultado:,.2f} metros")
print(f"{longitud:,.4f} metros, equivalen a {resultado:,.4f} {uni}")