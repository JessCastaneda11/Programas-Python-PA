# p009-promedio-de-calificaciones
# # Objetivo: Calcular el promedio de tres calificaciones ingresadas por el usuario.

print("Calculando el promedio de tres calificaciones:\n")

# SOLICITAR 3 CALIFICACIONES SEPARADAS POR ESPACIOS
cal1, cal2, cal3 = input().split() # SE ALMACENA CADA VALOR POR SEPARADO EN BASE AL ESPACIO (COMO CADENA)
print(type(cal1),type(cal2),type(cal3))
cal1, cal2, cal3 = int(cal1), int(cal2), int(cal3) #CONVERTIR CADA VARIABLE DE CADENA A ENTERO
print(type(cal1),type(cal2),type(cal3))

# CALCULAR EL PROMEDIO
suma = (cal1 + cal2 + cal3)
promedio = suma / 3

# MOSTRAR EL RESULTADO
print(f"Las calificaciones son: {cal1}, {cal2}, {cal3}")
print(f"La suma es: {suma}")
print(f"El promedio es: {promedio}")


