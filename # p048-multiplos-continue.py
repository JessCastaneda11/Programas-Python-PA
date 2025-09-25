# p048-multiplos-continue

# Imprime solo los multiplos de 10 hasta el 200

print('\033[2J\033[H')
print("Buscando múltiplos de 10 entre 1 y 200")

c = 0

while c <= 200:
    c += 1
    if c % 10 != 0:
        continue # Ignora todo lo que sigue y salta a la siguiente iteración
    
    # solo se ejecuta si el número es múltiplo de 10
    print(f' {c}', end='')

print("\nBúsqueda Terminada ...")