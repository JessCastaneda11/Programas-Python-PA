# p123-conjunto-personas

""""
Dadas las siguientes dos listas de nombres:
• Lista 1: Juan, Maria, Pedro, Jose, Rocio
• Lista 2: Pedro, Juan, Pablo, Mateo, Esther

Instrucciones:
1. Crear y mostrar los conjuntos A (basado en la Lista 1) y B (basado en la Lista 2).
2. Calcular y mostrar los resultados de las siguientes operaciones:

o Unión (A | B)
o Intersección (A & B)
o Diferencia (A - B)
o Diferencia Simétrica (A ^ B)

3. Verificar y mostrar el resultado (Verdadero/Falso) de las siguientes afirmaciones:
o ¿Es {Pablo, Mateo} un subconjunto de B?
o ¿Es A un superconjunto de {Reynaldo, Angelica}?
o ¿Está "Pedro" en el conjunto A?
o ¿No está "Lilia" en el conjunto B?

"""

print("\033[H\033[J")
print("Operaciones con Conjuntos de Personas\n")

lista1 = ["Juan", "Maria", "Pedro", "Jose", "Rocio"]
lista2 = ["Pedro", "Juan", "Pablo", "Mateo", "Esther"]

A = set(lista1)
B = set(lista2)

print("Conjunto A:", A)
print("Conjunto B:", B)

print("\n--- Operaciones ---")
print("Unión (A | B):", A | B)
print("Intersección (A & B):", A & B)
print("Diferencia (A - B):", A - B)
print("Diferencia Simétrica (A ^ B):", A ^ B)


print("\n--- Verificación de Afirmaciones ---")

afirm1 = {"Pablo", "Mateo"}.issubset(B)
print("¿{Pablo, Mateo} ⊆ B?:", afirm1)

afirm2 = A.issuperset({"Reynaldo", "Angelica"})
print("¿A ⊇ {Reynaldo, Angelica}?:", afirm2)

afirm3 = "Pedro" in A
print("¿'Pedro' ∈ A?:", afirm3)

afirm4 = "Lilia" not in B
print("¿'Lilia' ∉ B?:", afirm4)

print("\nProceso Terminado.")