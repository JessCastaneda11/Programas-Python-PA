# p106-calificaciones-estudiante

# Gestionar las calificaciones de un estudiante usando diccionarios

print('\033[2J\033[H')
print("Gestionar las calificaciones de un estudiante usando diccionarios")

materias = ['Física', 'Química', 'Matemáticas', 'Geografía', 'Estadística']
califs = [10, 9, 8, 7.5, 6]

print(f"Lista de materias     : \n{materias}")
print(f"Lista de calficaciones: \n{califs}")

notas = dict(zip(materias, califs))

print(f"\nLas notas: {notas} - {len(notas)}")

notas.update({'Ingles':10, 'Programación': 7})

print(f"\nLas notas: {notas} - {len(notas)}")

notas.pop('Física')
notas.popitem()

print(f"\nLas notas: {notas} - {len(notas)}")

notas.update({'Química':10, 'Matemáticas':10})

print(f"\nLas notas: {notas} - {len(notas)}")

s = 0

print("\nMaterias y calificaciones finales")

for m, c in notas.items():
    print(f'{m:<12} - {c:>5,.2f}')

    s = s + c

print(f"\nLa suma es: {s}")
print(f"\nEl promedio es: {s/len(notas)}")

notas.clear()
print(f"\nLas notas {notas} - {len(notas)}")