# p109-conversion-divisas
 
# Conversor de divisas a pesos mexicanos

print('\033[2J\033[H')
print("Conversor de divisas a pesos mexicanos")

conv = {
    'USD': 20.50,
    'EUR': 22.30,
    'GBP': 25.80,
    'JPY': 0.19,
    'CAD': 16.20
}

print("\nOpciones de cambio de moneda a pesos mexicanos MXN")
for m in conv:
    print(f"- {m}")

while True:
    moneda = input("Ingresa la moneda a convertir: ").upper()

    if moneda in conv: break
    continue

while True:
    try:
        cant = float(input(f"Ingresa la cantidad en {moneda}: "))

        if cant > 0: break

    except ValueError:
        print("Entrada no válida")

res = cant * conv[moneda]

print(f"{cant:,.2f} {moneda} equivale a {res:,.2f} MXN")