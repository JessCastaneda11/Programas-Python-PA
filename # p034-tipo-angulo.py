# p034-tipo-angulo

# Mostrar el tipo de ángulo según su medida en grados.
# < 90° "Agudo", = 90° "Recto", < 180° "Obtuso", = 180° "Llano", < 360° "Cóncavo", = 360° "Completo"


print('\033[2J\033[H')
print('--- Clasificador de Ángulos según su magnitud ---')

angulo = int(input("Dame un ángulo en grados: "))

if angulo < 0 or angulo > 360:
    print(f"Tu ángulo de {angulo} grados, no está en el rango de 0° a 360°, por lo tanto es INVALIDO")

else:

    if angulo < 90:
        print(f"El ángulo de {angulo} grados es un ángulo AGUDO")

    elif angulo == 90:
        print(f"El ángulo de {angulo} grados es un ángulo RECT0")

    elif angulo < 180:
        print(f"El ángulo de {angulo} grados es un ángulo OBTUSO")

    elif angulo == 180:
        print(f"El ángulo de {angulo} grados es un ángulo LLANO")
    
    elif angulo < 360:
        print(f"El ángulo de {angulo} grados es un ángulo CONCAVO")
    
    else:
        print(f"El ángulo de {angulo} grados es un ángulo COMPLETO")
    
print("\nProceso Terminado...")  