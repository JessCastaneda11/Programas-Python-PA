# p105-datos-estudiante

# Gestionar datos de un estudiante usando diccionarios.

print('\033[2J\033[H')
print("Gestión de Datos de un Estudiante")

estudiante = {
    'Nombre': 'Juan Pérez',
    'Edad': 45,
    'email': 'jperez@msn.com',
    'Carrera': 'Sistemas'
}

print(f"\nLos datos del estudiante son:\n\n {estudiante} - {len(estudiante)}")

estudiante['calificacion'] = 9.5
estudiante['email'] = 'juanp@gmail.com'
print(f"\nLos datos del estudiante son:\n\n {estudiante} - {len(estudiante)}")

print("\nIterar por las llaves (keys): ")

for k in estudiante.keys():
    print(k)

print("\nIterar por los valores (values): ")

for v in estudiante.values():
    print(v)

print("\nIterar por los elementos (items): ")

for k, v in estudiante.items():
    print(f"{k:<15} : {v}")