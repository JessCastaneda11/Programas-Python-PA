# p093-procesar-calificaciones

# Procesar las calificaciones de un alumno, usando una lista

print('\033[2J\033[H')
print("Procesar las calificaciones de un alumno.")

calificaciones = []

while True:
    try:
        cal = float(input("Calificación: "))

        if cal == 99: break
        
        if 0 <= cal <= 10:
            calificaciones.append(cal)
        
        else:
            print("Calificación NO valida.")
    
    except:
        print("¡Error! Entrada NO valida.")

if not calificaciones:
    print("No se capturaron calificaciones.")

else:
    suma = sum(calificaciones)
    promedio = suma / len(calificaciones)
    mayores_promedio = []

    for cal in calificaciones:

        if cal > promedio:
            mayores_promedio.append(cal)

print(f"Se capturaron {len(calificaciones)} calificaciones.")
print(f"Las calificaciones fueron: {calificaciones}")
print("\nEstadisticas del curso.")
print(f"Suma    : {suma}")
print(f"Promedio: {promedio}")
print(f"Calificaciones mayores al primedio: {len(mayores_promedio)} y son {mayores_promedio}")
print(f"Calificación más alta: {max(calificaciones)}")
print(f"Calificación más baja: {min(calificaciones)}")