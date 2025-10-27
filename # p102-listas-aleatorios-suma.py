# p102-listas-aleatorios-suma

# Generar 2 listas de 10 números aleatorios cada una. Crear una tercera lista donde el elemento sea la suma de los correspondientes de las listas A y B, solo si AMBOS elementos son impares; de lo contrario, el elemento de la tercera lista será 0. Imprimir las 3 listas.


import random

print('\033[2J\033[H')
print("Listas Aleatorias y Suma Condicional\n")

lista_a = []
lista_b = []
lista_c = []

i = 0
while i < 10:
    lista_a.append(random.randint(1, 20))
    lista_b.append(random.randint(1, 20))
    i += 1

i = 0
while i < 10:
    a = lista_a[i]
    b = lista_b[i]

    if a % 2 != 0 and b % 2 != 0:
        lista_c.append(a + b)
    else:
        lista_c.append(0)
    
    i += 1

print("--- Listas Generadas ---")
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")

print("\n--- Resultados (Suma solo si A[i] y B[i] son ambos impares) ---")
print(f"Lista C: {lista_c}")

print("\nProceso Terminado.")