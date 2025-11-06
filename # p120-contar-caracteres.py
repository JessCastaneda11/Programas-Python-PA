# p120-contar-caracteres

# Escribe un programa que pida al usuario una cadena de texto.
# Crea un diccionario vacío para almacenar la frecuencia (cantidad de apariciones) de cada carácter.
# Itera sobre cada carácter en la cadena ingresada.
#   - Si el carácter no existe como llave en el diccionario, agrégalo con un valor de 1.
#   - Si el carácter ya existe, incrementa su valor actual en 1.
# Al finalizar el ciclo, muestra el diccionario resultante con el conteo de caracteres.

print('\033[H\033[J')
print("Contar caracteres en una cadena\n")

cadena = input("Ingrese una cadena: ")
frecuencia = {}

for c in cadena:
    if c in frecuencia:
        frecuencia[c] += 1
    else:
        frecuencia[c] = 1

print("Resultado:")
print(frecuencia)