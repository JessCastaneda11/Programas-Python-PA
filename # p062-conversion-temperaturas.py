# p062-conversion-temperaturas

# El usuario debe introducir una temperatura inicial y una final en grados Celsius. El programa mostrará la conversión a grados Fahrenheit para cada grado en ese rango, incrementando de uno en uno.


while True:
    print("\033[H\033[J")
    print("Conversión de temperaturas dec Celsius a Fahrenheit")
    print("-"*60)

    temperatura_inicial = int(input("\nIntroduce la temperatura inicial en °C: "))
    temperatura_final = int(input("\nIntroduce la temperatura final en °C: "))

    temp = temperatura_inicial

    while temp <= temperatura_final:
        fahrenheit = (temp * 9/5) + 32
        print(f"{temp}°C = {fahrenheit:.2f}°F")
        temp += 1

    
    if input("\n¿Desea continuar (S/N)? ").upper() == "N": break

print("\nProceso Terminado")