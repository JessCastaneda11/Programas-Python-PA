# p137-temperatura

def centigrados_farenheit(c: float) -> float:
    return (c * 9 / 5) + 32

def farenheit_centigrados(f: float) -> float:
    return (f - 32) * 5 / 9

def main() -> None:
    print('\033[H\033[J')
    print('Conversion de temperaturas')
    print('1. Centigrados a Farenheit')
    print('2. Farenheit a Centigrados')
    op = int(input('Elige > '))
    if op == 1:
        print('Dame los Centigrados: ')
        c = float(input())
        f = centigrados_farenheit(c)
        print(f'{c} centigrados son {f} farenheit')
    elif op == 2:
        print('Dame los Farenheit: ')
        f = float(input())
        c = farenheit_centigrados(f)
        print(f'{f} farenheit son {c} centigrados')
    else:
        print('Opcion invalida')

if __name__ == "__main__":
    main()