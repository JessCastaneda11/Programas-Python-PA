# p135-numero-mayor

def numero_mayor(n1: int, n2: int, n3: int) -> int:
    may = n1
    if n2 > may:
        may = n2
    elif n3 > may:
        may = n3
    return may

#print(f'El mayor de 10,20,30: {numero_mayor(10,20,30)}')
#print(f'El mayor de -1,8,3: {numero_mayor(-1,8,3)}')

print('Dame tres numeros separados por enter')
a, b, c = int(input()), int(input()), int(input())
print(f'El mayor es { numero_mayor(a,b,c) }')