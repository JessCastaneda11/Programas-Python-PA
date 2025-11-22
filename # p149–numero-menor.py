# p149–numero-menor

# Programa que pide 3 numeros enteros y devuelve el menor

def numero_menor() -> int:
    print('Introduce el primer número: ', end='')
    n1 = int(input())

    print('Introduce el segundo número: ', end='')
    n2 = int(input())

    print('Introduce el tercer número: ', end='')
    n3 = int(input())

    # Calcula el menor de los tres
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3

    return menor


def main() -> None:
    print('\033[H\033[J')
    menor = numero_menor()
    print(f'El número menor es: {menor}')


if __name__ == "__main__":
    main()