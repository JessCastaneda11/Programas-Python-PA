# p041-aceptar-estudiante-v2

# La "Universidad Kitty Kat SA" solo acepta estudiantes que cumplan con los siguientes requisitos: 
# Ser mujer, ser mayor de 21 años y tener un promedio entre 8 y 9.5. 
# Escribe un programa que solicite el nombre, sexo (h/m), edad y tres calificaciones de un aspirante. El programa debe evaluar los datos y mostrar un mensaje claro que indique si el estudiante fue aceptado. Si no es aceptado, el mensaje debe especificar la razón del rechazo (ya sea por no cumplir con el sexo, la edad o el promedio requerido).

print('\033[2J\033[H')
print('--- INGRESO A LA UNIVERSIDAD  ---')

print("\nIngresa tus datos por favor: ")
nombre = input("\nNombre: ")
sexo = input("Sexo [H] / [M]: ").upper()
edad = int(input("Edad: "))
print("\nIngresa 3 calificaciones: ")
cal1, cal2, cal3 = input().split()
cal1, cal2, cal3 = float(cal1), float(cal2), float(cal3)

promedio = (cal1 + cal2 + cal3) / 3
#print(promedio)

if sexo != "M":
    print(f"\nLo sentimos, {nombre}. La universidad solo acepta mujeres.")

elif edad <= 21:
    print(f"\nLo sentimos, {nombre}. No cumples con la edad requerida (mayores de 21 años).")

elif promedio < 8:
    print(f"\nLo sentimos, {nombre}. Tu promedio de {promedio:.2f} no alcanza el mínimo requerido de 8.")

elif promedio > 9.5:
    print(f"\nLo sentimos, {nombre}. Tu promedio de {promedio:.2f} excede el máximo permitido de 9.5.")

else:
    print(f"\n¡Felicidades, {nombre}! Has sido aceptada. Cumples con la edad y tu promedio de {promedio:.2f} está dentro del rango permitido.")

print("\nProceso Terminado...")