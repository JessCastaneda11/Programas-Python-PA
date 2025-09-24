# p032-aceptar-estudiante

# Aceptar a un estudiante en base a la edad y 2 calificaciones.
# Usando la función lógica OR

print('\033[2J\033[H')
print('--- Admisión de Estudiantes a la Universidad ---')

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

if edad < 18:
    print(f"Lo sentimos, {nombre}, solo aceptamos mayores de edad, y tú tienes tan solo {edad} años")
else: 
    print("Ingresa 2 calificaciones separadas por un enter: ")
    calificacion1 = float(input())
    calificacion2 = float(input())

    if calificacion1 < 8 or calificacion2 < 8:
        print(f"Lo sentimos, se requieren 2 calificaciones de 8 como mínimo, y tú tienes {calificacion1} y {calificacion2}")

    else:
        print(f"Bienvenido {nombre}, tu edad {edad} y tus calificaciones: {calificacion1}, {calificacion2} te permiten ingresar")
        
print("\nProceso Terminado...")