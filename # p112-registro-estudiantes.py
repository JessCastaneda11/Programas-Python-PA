# p112-registro-estudiantes

# Crear una lista de diccionarios

grupo = [
    {'nombre':'Carlos','edad':45,'carrera':'sistemas','promedio':9} ,
    {'nombre':'Rocio','edad':35,'carrera':'sistemas','promedio':10}
]

print('\033[H\033[J')
print('Registro de Estudiantes\n')

print(f"Grupo: {grupo} - {len(grupo)}")

print("\nCapturar estudiantes")

while True:
    print(f"Datos del Estudiante")
    datos = {}
    nombre = input("Nombre: ")

    if nombre == '': break

    datos ['nombre'] = nombre
    datos ['edad'] = int(input("Edad: "))
    datos ['carrera'] = input("Carrera: ")
    datos ['promedio'] = float(input("Promedio: "))
    grupo.append(datos)

print(f"Grupo: {grupo} - {len(grupo)}")

print(f"\n\nDatos en forma de tabla")
print("-"*60)

for k in grupo[0].keys():
    print(f'{k:>12}', end='')

print()
print("-"*60)

for alumno in grupo:
    for v in alumno.values():
        print(f'{v:>12}', end='')
    print()
print("-"*60)

print("\n\nDatos en forma de registro")
print("-"*60)
suma = sumae = 0
for alumno in grupo:
    suma = suma + alumno['promedio']
    sumae = sumae + alumno['edad']
    for k,v in alumno.items():
        print(f"{k:<12} : {v:>12}")
    print()
print("-"*60)

print(f"\nSuma         : ", suma)
print("Promedio Calif  : ", suma/len(grupo))
print("Promedio Edades : ", sumae/len(grupo))