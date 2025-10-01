# p056-contador-vocales

# Cuenta vocales, consonantes y otros caracteres en una frase

while True:
    print('\033[H\033[J')
    print("Contador de vocales y consonantes \n")

    frase = input("Introduce una frase: ")

    print(len(frase)) # Muestra en pantalla la longitud de la frase, es decir, cuántos caracteres tiene en total.

    vocales = consonantes = otros = 0
    indice = 0

    while indice < len(frase):
        caracter = frase[indice] # Tomamos el caracter correspondiente de la frase

        if caracter >= 'a' and caracter <= 'z': # Verificamos que sea una letra

            if caracter in 'aeiou': # Es vocal
                vocales += 1
            
            else: # Es consonante
                consonantes += 1
        
        else: # Es cualquier otra cosa
            otros += 1
        
        indice += 1  # Se pasa al siguiente caracter
    
    print(f"Analisis de la frase")
    print(f"Número de vocales: {vocales}")
    print(f"Número de consonantes: {consonantes}")
    print(f"Número de otros: {otros}")

    if input("\nDeseas continuar? (S/N)").upper() == 'N': break

print("\nProceso Terminado")