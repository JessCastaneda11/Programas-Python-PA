# p124-conjunt-numeros

"""
Dadas las siguientes tres listas de números:
• Lista 1: 50, 60, 70, 80, 90, 100, 200
• Lista 2: 60, 90, 100, 300, 400, 500
• Lista 3: 10, 20, 60, 90, 70, 100, 600, 700

Instrucciones:
1. Crear y mostrar los conjuntos A, B y C a partir de las listas.
2. Calcular y mostrar los resultados de las siguientes operaciones:

o Unión (A | B)
o Unión (B | C)
o Diferencia (A - C)
o Diferencia Simétrica (B ^ C)
o Intersección (B & C)

3. Verificar y mostrar el resultado (Verdadero/Falso) de las siguientes preguntas:
o ¿Es A subconjunto de B?
o ¿Es C subconjunto de A?
o ¿Está el número 100 en A?
o ¿Está el número 60 en A, B y C?
o ¿No está el número 900 en C?

"""

print("\033[H\033[J")
print("Operaciones con Conjuntos Numéricos\n")

lista1 = [50, 60, 70, 80, 90, 100, 200]
lista2 = [60, 90, 100, 300, 400, 500]
lista3 = [10, 20, 60, 90, 70, 100, 600, 700]

A = set(lista1)
B = set(lista2)
C = set(lista3)

print("Conjunto A:", A)
print("Conjunto B:", B)
print("Conjunto C:", C)

print("\n--- Operaciones ---")
print("Unión (A | B):", A | B)
print("Unión (B | C):", B | C)
print("Diferencia (A - C):", A - C)
print("Diferencia Simétrica (B ^ C):", B ^ C)
print("Intersección (B & C):", B & C)

print("\n--- Verificación de Afirmaciones ---")
print("¿A es subconjunto de B?:", A.issubset(B))
print("¿C es subconjunto de A?:", C.issubset(A))
print("¿Está el número 100 en A?:", 100 in A)
print("¿Está el número 60 en A, B y C?:", (60 in A) and (60 in B) and (60 in C))
print("¿No está el número 900 en C?:", 900 not in C)

print("\nProceso Terminado.")