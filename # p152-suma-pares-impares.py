# p152-suma-pares-impares

# Suma numeros pares o impares dentro de un rango

def suma_rango(inicio: int, fin: int, tipo: str) -> int:
    suma = 0
    for n in range(inicio, fin + 1):
        if tipo == 'P' and n % 2 == 0:
            suma += n
        elif tipo == 'I' and n % 2 != 0:
            suma += n
    return suma


def main() -> None:
    print('\033[H\033[J')
    print('*** Suma en Rango ***')
    inicio = int(input('Introduce el número inicial: '))
    fin = int(input('Introduce el número final: '))
    tipo = input('¿Qué deseas sumar? (P)ares o (I)mpares: ').upper()

    if tipo not in ('P', 'I'):
        print('Error: Debes elegir P o I.')
        return

    resultado = suma_rango(inicio, fin, tipo)

    texto = 'pares' if tipo == 'P' else 'impares'
    print()
    print(f'La suma de los números {texto} entre {inicio} y {fin} es: {resultado}')


if __name__ == '__main__':
    main()