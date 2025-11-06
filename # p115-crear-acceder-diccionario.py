# p115-crear-acceder-diccionario

# Crea un diccionario llamado días usando llaves numéricas para los días de la semana.
# Muestra el diccionario completo.
# Accede y muestra los valores de las llaves 1 y 7 usando [],
# y también usando el método get().
# Finalmente vuelve a mostrar el diccionario completo.

print('\033[H\033[J')
print("Acceder a elementos de un diccionario\n")

dias = {
    1: 'Lunes',
    2: 'Martes',
    3: 'Miércoles',
    4: 'Jueves',
    5: 'Viernes',
    6: 'Sábado',
    7: 'Domingo'
}

print("Diccionario inicial:")
print(dias)

print("\nAccediendo a elementos:")
print("Llave 1 (con []):", dias[1])
print("Llave 7 (con []):", dias[7])
print("Llave 5 (con get()):", dias.get(5))
print("Llave 7 (con get()):", dias.get(7))

print("\nDiccionario final:")
print(dias)