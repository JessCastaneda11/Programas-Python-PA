# p155-estadisticas-basicas

# Calcula estadisticas basicas de una lista de numeros

from typing import List
import math

def leer_lista() -> List[int]:
    entrada = input('Dame números (separados por espacio): ')
    partes = entrada.split()
    nums: List[int] = []
    for p in partes:
        nums.append(int(p))
    return nums

def mayor(lista: List[int]) -> int:
    m = lista[0]
    for n in lista:
        if n > m:
            m = n
    return m

def menor(lista: List[int]) -> int:
    m = lista[0]
    for n in lista:
        if n < m:
            m = n
    return m

def media(lista: List[int]) -> float:
    suma = 0
    for n in lista:
        suma += n
    return suma / len(lista)

def varianza(lista: List[int]) -> float:
    prom = media(lista)
    suma = 0
    for n in lista:
        suma += (n - prom) ** 2
    return suma / len(lista)

def desviacion(lista: List[int]) -> float:
    return math.sqrt(varianza(lista))

def main() -> None:
    print('\033[H\033[J')
    nums = leer_lista()

    print(f'Lista de números: {nums}\n')

    print('Estadísticas:')
    print(f'Media               : {media(nums):.3f}')
    print(f'Mayor               : {mayor(nums)}')
    print(f'Menor               : {menor(nums)}')
    print(f'Varianza            : {varianza(nums):.3f}')
    print(f'Desviación estándar : {desviacion(nums):.3f}')

if __name__ == '__main__':
    main()