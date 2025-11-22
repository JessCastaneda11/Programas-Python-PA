# p132-funcion-retorno

# funcion que regresa valores

def suma(n1:float, n2:float, n3:float) -> float:
    return n1 + n2 + n3

suma_resultado = suma(100.30,200.20,300.50)
print(f'La suma es : {suma_resultado:.2f}')

print('Dame tres numeros floantes separados enter:')
a, b, c = float(input()), float(input()), float(input())
print(f'La suma de los numeros es { suma(a,b,c):.2f }')