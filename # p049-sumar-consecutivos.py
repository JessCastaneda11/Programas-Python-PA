# p049-sumar-consecutivos

# Suma números consecutivos hasta alcanzar 100

print('\033[2J\033[H')
print("Rifa entre amigos para recaudar 100, ¿cuántos boletos necesito?")

c = 0
suma = 0

while c < 200:
    c += 1
    suma += c
    meta = 5000

    print(f" {c}", end='')

    if suma >= meta:
        print("\n\n¡Meta Alcanzada!")
        print(f"Boletos: {c}")
        break

print("\nProceso terminado ..." + str(suma))