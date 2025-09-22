# p028-retira-cuenta

# Simula el retiro de dinero de una cuenta de ahorros, revisa el saldo

saldo_actual = 15000

print("Simulacro de retiro")

print('\033[2J\033[H')
print(f"Tu saldo inicial es {saldo_actual:.2f}")

cantidad_retiro = float(input("Cantidad a retirar: "))

if cantidad_retiro > 0:
    if cantidad_retiro <= saldo_actual:
        print("Iniciando con el retiro...")
        saldo_actual -= cantidad_retiro
        print("Retiro Exitoso")
        print(f"Tu nuevo saldo es {saldo_actual:.2f}")
    else:
            print("\nFondos insuficientes para completar la transacción")
else:
    print("\nLa cantidad a retirar debe ser un número positivo")

print("\nProceso Terminado...")