# p026–convertir-temperaturas-v2

# Convertir temperaturas de grados celsius a fahrenheit y viceversa

print('\033[2J\033[H')
print('\033[31mConvertir de Grados Celsius a Grados Fahrenheit\033[0m')

print('\033[34m')
print("[C] elsius a Fahrenheit")
print("[F] ahrenheit a Celsius")
print('\033[0m')

op = input("Elige ? ").upper()

if op == "C":
    print("\nConvirtiendo de Celsius a Fahrenheit🌡️")
    c = float(input("Introduce los Grados Celsius: "))
    f = (c * 9 / 5) + 32
    print(f"\n{c:.2f} grados Celsius, equivale a {f:.2f} grados fahrenheit") 
else: 
    if op == "F":
        print("\nConvirtiendo de Fahrenheit a Celsius🌡️")
        f = float(input("Introduce los Grados Fahremheit: "))
        c = (f - 32) * 5 / 9
        print(f"\n{f:.2f} grados Fahrenheit, equivale a {c:.2f} grados celsius") 
    else:
        print("❌ OPCIÓN INVALIDA")

print("\nPrograma finalizado...")