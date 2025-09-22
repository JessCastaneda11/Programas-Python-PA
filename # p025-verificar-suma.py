# p025-verificar-suma

# Verificar si la suma de dos números es igual a un tercero

print("-"*60)
print("Verificar si la suma de dos números es igual a un tercero 🤔")
print("-"*60)

# ENTRADA
print("\nDame 3 números enteros:")

n1 = int(input("Número 1 ? "))
n2 = int(input("Número 2 ? "))
n3 = int(input("Número 3 ? "))

# PROCESO
suma = n1 + n2

if suma == n3:
    print(f"\n ✅ ¡Correcto! {n1} + {n2} ES IGUAL {n3} ")

else:
    print(f"\n ❌ No coinciden {n1} + {n2} NO ES IGUAL {n3} ")

print("-"*60)
print("\nFin del programa")