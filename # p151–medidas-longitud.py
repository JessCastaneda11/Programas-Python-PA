# p151–medidas-longitud

# Conversor de unidades de longitud

def pulgadas_a_centimetros(pulg: float) -> float:
    return pulg * 2.54

def metros_a_pies(m: float) -> float:
    return m * 3.281

def main() -> None:
    print('\033[H\033[J')
    print('*** Conversor de Unidades ***')
    print('1. Pulgadas a Centímetros')
    print('2. Metros a Pies')
    print('3. Salir')

    op = int(input('Elige una opción: '))

    if op == 1:
        pulg = float(input('Introduce la cantidad en pulgadas: '))
        cm = pulgadas_a_centimetros(pulg)
        print(f'{pulg} pulgadas equivalen a {cm} centímetros.')

    elif op == 2:
        m = float(input('Introduce la cantidad en metros: '))
        pies = metros_a_pies(m)
        print(f'{m} metros equivalen a {pies} pies.')

    elif op == 3:
        print('Adiós...')
    else:
        print('Opción inválida')

if __name__ == "__main__":
    main()