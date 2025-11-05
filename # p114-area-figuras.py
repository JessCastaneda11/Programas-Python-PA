# p114-area-figuras

# Crear un diccionario de diccionarios

import math

figuras = {
    "Circulo": {"radio": 0, "formula": "math.pi * r ** 2"},
    "Triangulo": {"base": 0, "altura": 0, "formula": "0.5 * b * a"},
    "Rectangulo": {"largo": 0, "ancho": 0, "formula": "l * a"}
}

print("\033[H\033[J")
print("Área de Figuras Geométricas\n")

print("\nFiguras Disponibles")

for k,v in figuras.items():
    print(f"{k:<10} - Fórmula: {v['formula']}")

while True:

    fig = input("\nElige una figura: ").title()

    if fig in figuras: break

    print("x")

area = 0

if fig == 'Circulo':
    r = int(input('Radio : '))
    area = eval(figuras[fig]['formula'].replace('r', str(r)))
    print(f"Formula: {figuras[fig]['formula']}")

elif fig=='Triangulo':
    b = float(input('Base : '))
    a = float(input('Altura : '))
    area = eval(figuras[fig]['formula'].replace('b', str(b)).replace('a',str(a)))
    print(f"Formula: {figuras[fig]['formula']}")

elif fig=='Rectangulo':
    l = float(input('Largo : '))
    a = float(input('Ancho : '))
    area = eval(figuras[fig]['formula'].replace('l', str(l)).replace('a',str(a)))
    print(f"Formula: {figuras[fig]['formula']}")

print(f"\nEl área de {fig} es: {area:.4f}")