# p051-adivina-numero

# Simula un juego de azar donde el usuario adivina un número entre 1 y 50

import random

print('\033[2J\033[H')
print("Bienvenido al juego de Adivina el número")
print("Yo te doy un número entre 1 y 50, y tú tratas de adivinarlo")

numero_secreto = random.randint(1,50)
intento_usuario = 0
contador_intentos = 0

while True:
    intento_usuario = int(input("Tu número: "))
    contador_intentos += 1

    if intento_usuario < numero_secreto:
        print("Demasiado bajo, intenta con un número más alto")
    
    elif intento_usuario > numero_secreto:
        print("Demasiado alto, intenta con un número más bajo")

    else:
        print(f"\n¡Felicidades! ¡Adivinaste! El número secreto era {numero_secreto}")
        print(f"Lo lograste en {contador_intentos} intentos")
        break

print("\nJuego Terminado...")