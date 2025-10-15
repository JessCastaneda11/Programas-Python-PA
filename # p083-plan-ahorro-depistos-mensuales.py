# p083-plan-ahorro-depistos-mensuales

# El programa simulará un plan de ahorro. Deberá solicitar al usuario un monto inicial, un depósito mensual fijo, una tasa de interés mensual (porcentaje), y el número total de meses del plan. El programa debe mostrar una tabla que detalle, para cada mes, el saldo inicial, el interés ganado en ese mes, y el saldo final. El interés se calcula sobre el saldo inicial antes de sumar el nuevo depósito.

while True:
    print('\033[2J\033[H') 
    print("Simulación de Plan de Ahorro con Depósitos Mensuales\n")

    monto_inicial = float(input("Monto inicial de ahorro: "))
    deposito_mensual = float(input("Depósito mensual: "))
    tasa_interes = float(input("Tasa de interés mensual (%): "))
    meses = int(input("Número de meses a simular: "))

    print("\n--- Plan de Ahorro Detallado ---")
    print("Mes | Saldo Inicial  | Interés   | Saldo Final")
    print("-----------------------------------------------")

    saldo = monto_inicial

    for mes in range(1, meses + 1):
        interes = saldo * (tasa_interes / 100)
        saldo_final = saldo + interes + deposito_mensual   # Saldo final incluye el depósito
        print(f"Mes {mes}: Saldo Inicial: ${saldo:7.2f} | Interés: ${interes:5.2f} | Saldo Final: ${saldo_final:7.2f}")
        saldo = saldo_final  # El saldo final pasa a ser el saldo inicial del siguiente mes

    print(f"\nAl final de {meses} meses, tendrás ${saldo:,.2f}")

    continuar = input("\n¿Deseas realizar otra simulación? (S/N): ").upper()
    if continuar == "N": break

print("\nProceso Terminado...")