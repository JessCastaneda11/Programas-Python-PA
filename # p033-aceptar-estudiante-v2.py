# p033-aceptar-estudiante-v2

# Aceptar a un estudiante en base a la edad y 2 calificaciones.
# Usando la función lógica AND

print('\033[2J\033[H')
print('--- Admisión de Estudiantes a la Universidad ---')

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("El proceso continua...")
    print("Ingresa 2 calificaciones separadas por un enter: ")
    calificacion1 = float(input())
    calificacion2 = float(input())
    
    if calificacion1 >=8 and calificacion2 >=8:
        print(f"Bienvenido {nombre}, tu edad {edad} y tus calificaciones: {calificacion1}, {calificacion2} te permiten ingresar")
    
    else:
        print(f"Lo sentimos, se requieren 2 calificaciones de 8 como mínimo, y tú tienes {calificacion1} y {calificacion2}")
else:
    print(f"\nLo sentimos {nombre}, solo aceptamos mayores de edad y tú tienes solo {edad} años")

print("\nProceso Terminado...")