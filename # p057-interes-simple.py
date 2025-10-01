# p057-interes-simple

# Calcular los años necesarios para alcanzar una meta de ahorro con un interés simple.

while True:
    print('\033[H\033[J')
    print("Calculadora de años para meta de ahorro con interés simple")
    print("-"*60)

    capital_inicial = float(input("Capital Inicial: "))
    tasa_interes = float(input("Tasa de Interés Anual: "))
    meta_ahorro = float(input("Meta de Ahorro: "))

    capital_actual = capital_inicial
    años = 0
    interes_anual_fijo = capital_inicial * (tasa_interes / 100)

    while capital_actual <= meta_ahorro:
        capital_actual += interes_anual_fijo
        años += 1
    
    print("-"*60)
    print(f"Para alcanzar $ {meta_ahorro}, necesitas {años} años")
    print(f"El monto final será de: {capital_actual}")


    if input("\nDeseas continuar? (S/N)").upper() == 'N': break

print("\nProceso Terminado")