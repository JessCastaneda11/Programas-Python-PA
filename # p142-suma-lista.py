# p142-suma-lista

# Funcion que recibe una lista de flotantes y regresa su suma

from typing import List

def suma_lista(lista: List[float]) -> float:
    suma = 0
    for numero in lista:
        suma += numero
    return suma

numeros: List[float] = [1.5, 2.3, 3.7, 4.0]
resultado = suma_lista(numeros)
print(f'La suma de los numeros es {resultado}')