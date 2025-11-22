# p143-lista-pares

# Funcion que recibe una lista de numeros enteros y regresa una lista de los pares

from typing import List

def lista_pares(lista: List[int]) -> List[int]:
    pares: List[int] = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

numeros: List[int] = [1,2,3,4,5,6,7,8,9,10,12]
resultado: List[int] = lista_pares(numeros)
print(f'Los numeros pares de la lista son {resultado}')