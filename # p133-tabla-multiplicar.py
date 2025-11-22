# p133-tabla-multiplicar

# Imprime la tabla de multiplicar deseada, hasta el limite deseado, usando una funcion

def tabla_multiplicar(tabla:int, limite:int) -> None:
    print(f'Tabla de multiplicar del {tabla} hasta el {limite}!')
    for i in range(1, limite + 1):
        res = tabla * i
        print(f'{tabla} x {i} = {res}')
    print()

#tabla_multiplicar(5,10)
#tabla_multiplicar(3,20)

tabla = int(input('Ingresa la tabla de multiplicar que deseas (ej. 5): '))
limite = int(input('Ingresa el limite hasta donde deseas multiplicar (ej. 10): '))

tabla_multiplicar(tabla, limite)