#p040-calculo-notas

# Escribe un programa que calcule el promedio de 5 calificaciones ingresadas por el usuario. Basado en el promedio, el programa deberá mostrar uno de los siguientes mensajes:
# Menor a 6: "Quedas reprobado"
# Desde 6 hasta menos de 7: "Pasas de panzazo"
# Desde 7 hasta menos de 8: "Muy bien, puedes mejorar"
# Desde 8 hasta menos de 9: "Excelente, sigue así"
# Desde 9 hasta 10: "Perfecto, tu esfuerzo valió la pena"

print('\033[2J\033[H')
print('--- PROMEDIOS ---')

print("\nIngresa tus calificaciones separadas por un espacio:")

cal1, cal2, cal3, cal4, cal5 = input().split()
cal1, cal2, cal3, cal4, cal5 = float(cal1), float(cal2), float(cal3), float(cal4), float(cal5)

promedio = (cal1 + cal2 + cal3 + cal4 + cal5) / 5
print(f"\nTu promedio es: {promedio:.2f}")

if promedio >= 0 and promedio < 6:
    print("\nQuedas reprobado")
    
elif promedio >= 6 and promedio < 7:
    print("\nPasas de panzazo")

elif promedio >= 7 and promedio < 8:
    print("\nMuy bien, puedes mejorar")

elif promedio >= 8 and promedio < 9:
    print("\nExcelente, sigue así")

elif promedio >= 9 and promedio <= 10:
    print("\nPerfecto, tu esfuerzo valió la pena")

else:
    print("\nCalificaciones invalidas, intenta de nuevo")

print("\nProceso Terminado...")