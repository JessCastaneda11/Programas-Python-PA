# p154-calcula-factoriales

# Calcula el factorial de cada numero en una lista

from typing import List

def leer_lista() -> List[int]:
    entrada = input('Dame los números (separados por espacio): ')
    partes = entrada.split()
    numeros: List[int] = []
    for p in partes:
        numeros.append(int(p))
    return numeros

def factorial(num: int) -> int:
    if num <= 1:
        return 1
    res = 1
    for i in range(2, num + 1):
        res *= i
    return res

def procesar_lista(lista: List[int]) -> List[int]:
    nueva: List[int] = []
    for n in lista:
        nueva.append(factorial(n))
    return nueva

def main() -> None:
    print('\033[H\033[J')
    lista = leer_lista()
    nueva = procesar_lista(lista)

    print(f'La lista de números originales: {lista}')
    print(f'La lista con los factoriales: {nueva}')

if __name__ == '__main__':
    main()