# p153-suma-digitos

# Procesa una lista de numeros y devuelve otra lista con la suma de sus digitos

from typing import List

def leer_lista() -> List[int]:
    entrada = input('Dame los números (separados por espacio): ')
    partes = entrada.split()
    numeros: List[int] = []
    for p in partes:
        numeros.append(int(p))
    return numeros

def suma_digitos(num: int) -> int:
    s = 0
    for d in str(num):
        s += int(d)
    return s

def procesar_lista(lista: List[int]) -> List[int]:
    nueva: List[int] = []
    for n in lista:
        nueva.append(suma_digitos(n))
    return nueva

def main() -> None:
    print('\033[H\033[J')
    lista = leer_lista()
    nueva = procesar_lista(lista)

    print(f'La lista de números original      : {lista}')
    print(f'La lista con la suma de dígitos de los números: {nueva}')

if __name__ == '__main__':
    main()